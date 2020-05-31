from trailcache.coordmath import generate_bbox, distance_between
from trailcache.commandline import get_user_info, print_err, print_info, print_ok, init_colorama, ProgressBar
from trailcache.xmlparser import get_caches
import requests
import gpxpy
import gpxpy.gpx
import math
import sys
import os


def main():
    cache_arr = []

    init_colorama()
    settings = get_user_info(sys.argv)

    gpx_file = open(settings.get_input_path(), 'r')
    gpx = gpxpy.parse(gpx_file)

    print_info("waypoint interval: " +
               str(waypoint_interval(settings.get_request_limit(), gpx)))
    waypoint_count = 0

    pb = ProgressBar("requests sent", settings.get_request_limit())

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if waypoint_count == waypoint_interval(settings.get_request_limit(), gpx):
                    waypoint_count = 0
                    bbox = generate_bbox(
                        point.latitude, point.longitude, settings.get_search_radius())

                    pb.update()

                    temp = request_caches(settings.get_ge_token(), bbox)

                    for cache in temp:
                        if cache_not_in_list(cache_arr, cache):
                            cache_arr.append(cache)
                waypoint_count = waypoint_count + 1
    pb.close()

    print_info("found " + str(len(cache_arr)) + " unique caches")

    cache_arr = apply_filters(cache_arr, settings.get_filters(), gpx)

    print_info(str(len(cache_arr)) +
               " caches remaining after applying filters")
    print_info("starting download of gpx files")

    download_caches(cache_arr, settings)


def get_point_count(gpx):
    count = 0
    for track in gpx.tracks:
        for segment in track.segments:
            count += len(segment.points)
    return count


def waypoint_interval(limit, gpx):
    return math.floor(get_point_count(gpx)/limit)


def request_caches(token, bbox):
    url = "https://www.geocaching.com/datastore/googleearthutils.svc/kml/" + \
        token + "/search?BBOX=" + str(bbox[0]) + "," + \
        str(bbox[1]) + "," + str(bbox[2]) + "," + str(bbox[3])

    receive = requests.get(url)

    if receive.status_code != 200:
        print_err("there was a problem recieving data from geocaching.com")
        return
    return get_caches(receive.text)


def cache_not_in_list(cache_arr, cache):
    for obj in cache_arr:
        if obj.get_gc_code() == cache.get_gc_code():
            return False
    return True


def apply_filters(cache_arr, filters, gpx):
    temp_arr = []

    pb = ProgressBar("caches processed", len(cache_arr))

    for cache in cache_arr:
        if within_distance_limit(cache, filters.get_distance(), gpx):
            temp_arr.append(cache)
        pb.update()
    cache_arr = temp_arr
    temp_arr = []
    pb.close()
    return cache_arr


def within_distance_limit(cache, distance, gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if distance_between(point.latitude, point.longitude, cache.latitude, cache.longitude) <= distance:
                    return True
    return False


def download_caches(cache_arr, settings):
    for cache in cache_arr:
        url = "https://www.geocaching.com/play/map/api/gpx/" + cache.get_gc_code()
        cookie = "gspkauth=" + settings.get_gspk_auth_token()
        headers = {"Cookie": cookie}

        receive = requests.get(url, headers=headers)
        if receive.status_code != 200:
            print_err("there was a problem downloading geocache: " +
                      cache.get_gc_code())
        else:
            gpx_file = open(settings.get_output_path(), "w", encoding='utf-8')
            gpx_file.write(receive.text)
            print_info("downloaded geocache: " + cache.get_gc_code())
