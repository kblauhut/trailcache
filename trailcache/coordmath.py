import math


def generate_bbox(latitude, longitude, distance):
    lat_radian = math.radians(latitude)

    lat_km = 110.574235
    long_km = 110.572833 * math.cos(lat_radian)
    delta_lat = distance / 1000.0 / lat_km
    delta_long = distance / 1000.0 / long_km

    min_lat = latitude - delta_lat
    min_long = longitude - delta_long
    max_lat = latitude + delta_lat
    max_long = longitude + delta_long

    bbox = [min_lat, min_long, max_lat, max_long]
    return bbox


def distance_between(latitude1, longitude1, latitude2, longitude2):
    earth_radius = 6371

    delta_lat = math.radians(latitude2-latitude1)
    delta_long = math.radians(longitude2-longitude1)

    latitude1 = math.radians(latitude1)
    latitude2 = math.radians(latitude2)

    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.sin(delta_long/2) * \
        math.sin(delta_long/2) * math.cos(latitude1) * math.cos(latitude2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return math.floor(earth_radius * c * 1000)
