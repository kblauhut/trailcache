from trailcache.coordmath import generate_bbox, distance_between
from trailcache.commandline import get_user_info, print_err, print_info, print_ok
from trailcache.xmlparser import get_caches
import requests
import gpxpy
import gpxpy.gpx
import math

bbox_radius = 4000

gpx_file = open('gpx-test/test.gpx', 'r')
gpx = gpxpy.parse(gpx_file)


def main():
    cache_arr = []

    user_info = get_user_info()
    token = user_info[0]
    limit = user_info[1]
    distance = user_info[2]

    print_info("Waypoint interval: " + str(waypoint_interval(limit)))
    waypoint_count = 0
    query_count = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if waypoint_count == waypoint_interval(limit):
                    waypoint_count = 0
                    query_count = query_count + 1

                    bbox = generate_bbox(
                        point.latitude, point.longitude, bbox_radius)
                    temp = request_caches(token, bbox)
                    for cache in temp:
                        if cache_not_in_list(cache_arr, cache):
                            cache_arr.append(cache)
                    print_info("progress: " + str(query_count) +
                               "/" + str(limit) + " sent")
                waypoint_count = waypoint_count + 1
    print_info("found " + str(len(cache_arr)) + " unique caches")


def get_point_count():
    count = 0
    for track in gpx.tracks:
        for segment in track.segments:
            count += len(segment.points)
    return count


def waypoint_interval(limit):
    return math.floor(get_point_count()/limit)


def request_caches(token, bbox):
    url = "https://www.geocaching.com/datastore/googleearthutils.svc/kml/" + \
        token + "/search?BBOX=" + str(bbox[0]) + "," + \
        str(bbox[1]) + "," + str(bbox[2]) + "," + str(bbox[3])

    receive = requests.get(url)

    if receive.status_code == 200:
        print_ok("recieved geocache info for waypoint")
    else:
        print_err("there was a problem recieving data from geocaching.com")
        return
    return get_caches(receive.content)


def cache_not_in_list(cache_list, cache):
    for obj in cache_list:
        if obj.get_gc_code() == cache.get_gc_code():
            return False
    return True


def filter_caches():
    return
