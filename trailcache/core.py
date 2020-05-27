from trailcache.coordmath import generate_bbox, distance_between
from trailcache.commandline import get_user_info, print_err, print_info, print_ok
from trailcache.xmlparser import get_caches
import requests
import gpxpy
import gpxpy.gpx
import math

bbox_radius = 1000

gpx_file = open('gpx-test/test.gpx', 'r')
gpx = gpxpy.parse(gpx_file)


def main():
    user_info = get_user_info()
    token = user_info[0]
    limit = user_info[1]
    distance = user_info[2]

    print_info("Waypoint interval: " + str(waypoint_interval(limit)))
    i = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if i == waypoint_interval(limit):
                    i = 0
                    bbox = generate_bbox(
                        point.latitude, point.longitude, bbox_radius)
                    request_caches(token, bbox)
                i = i+1


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
    print(url)
    if receive.status_code == 200:
        print_ok("recieved geocache info for waypoint")
    else:
        print_err("there was a problem recieving data from geocaching.com")
        return
    get_caches(receive.content)
