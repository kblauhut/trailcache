from colorama import Fore
from trailcache.coordmath import generate_bbox, distance_between
import gpxpy
import gpxpy.gpx
import math

request_limit = 25

gpx_file = open('gpx-test/test.gpx', 'r')
gpx = gpxpy.parse(gpx_file)


def run_script(token, limit, distance):
    print(Fore.YELLOW + "Waypoint interval: " + str(waypoint_interval()))
    i = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if i == waypoint_interval():
                    i = 0
                    print('Point at ({0},{1})'.format(
                        point.latitude, point.longitude))
                i = i+1


def get_point_count():
    count = 0
    for track in gpx.tracks:
        for segment in track.segments:
            count += len(segment.points)
    return count


def waypoint_interval():
    return math.floor(get_point_count()/request_limit)
