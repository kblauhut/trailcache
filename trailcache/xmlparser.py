from trailcache.commandline import print_err, print_info, print_ok
from trailcache.struct import Cache
from io import StringIO
from xml.etree.ElementTree import Element, SubElement
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
    longitude = float(string[:index])
    latitude = float(string[index+1:])
    return [latitude, longitude]


def create_gpx():
    gpx = Element("gpx")
    gpx.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    gpx.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
    gpx.set("version", "1.0")
    gpx.set("creator", "Trailcache Pocket Query")
    gpx.set("xsi:schemaLocation", "http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd http://www.groundspeak.com/cache/1/0 http://www.groundspeak.com/cache/1/0/cache.xsd")
    gpx.set("xmlns", "http://www.topografix.com/GPX/1/0")
    return gpx


def append_cache(cache, gpx):
    it = element_tree.iterparse(StringIO(cache))

    for _, el in it:
        _, _, el.tag = el.tag.rpartition('}')
    cache_tree = it.root

    for child in cache_tree.findall("wpt"):
        cache = child.find("cache")
        cache.set("xmlns:groundspeak", "http://www.groundspeak.com/cache/1/0")
        for cacheinfo in list(cache.iter()):
            cacheinfo.tag = "groundspeak:" + cacheinfo.tag
        gpx.append(child)
    return gpx


def xml_write(xml, path):
    tree = element_tree.ElementTree(xml)
    tree.write(path, xml_declaration=True, encoding='utf-8')
