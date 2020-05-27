from trailcache.commandline import print_err, print_info, print_ok
from trailcache.cache import Cache
import xml.etree.ElementTree as element_tree

namespace = "{http://www.opengis.net/kml/2.2}"


def get_caches(xml):
    cache_arr = []
    root = element_tree.fromstring(xml)

    folder = root[0].find(namespace + "Folder")

    name = folder.find(namespace + "name")
    name_text = name.text.lower()
    if "no geocaches" in name_text:
        print_err("error returning geocaches, try later or check token")
        return []

    for subfolder in folder.findall(namespace + "Folder"):
        for child in subfolder.findall(namespace + "Placemark"):
            cache = cache_to_obj(child)
            cache_arr.append(cache)

    return cache_arr


def cache_to_obj(cache):
    lat_long = parse_lat_long(cache.find(namespace + "Point")[0].text)
    latitude = lat_long[0]
    longitude = lat_long[1]

    extended_data = cache.find(namespace + "ExtendedData")
    gc_code = extended_data.find("*[@name='gc_code']")[0].text
    cache_type = extended_data.find("*[@name='gc_wptTypeId']")[0].text
    container_id = extended_data.find("*[@name='gc_containerId']")[0].text
    difficulty = extended_data.find("*[@name='gc_difficulty']")[0].text
    terrain = extended_data.find("*[@name='gc_terrain']")[0].text

    return Cache(gc_code, latitude, longitude, cache_type, container_id, difficulty, terrain)


def parse_lat_long(string):
    index = string.index(",")
    latitude = string[:index]
    longitude = string[index+1:]
    return [latitude, longitude]
