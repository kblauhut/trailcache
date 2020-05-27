from trailcache.commandline import print_err, print_info, print_ok
import xml.etree.ElementTree as element_tree

namespace = "{http://www.opengis.net/kml/2.2}"


def get_caches(xml):
    root = element_tree.fromstring(xml)

    folder = root[0].find(namespace + "Folder")

    name = folder.find(namespace + "name")
    name_text = name.text.lower()
    if "no geocaches" in name_text:
        print_err("error returning geocaches - your token may be wrong")
        return
    else:
        print_info(name_text)

    for subfolder in folder.findall(namespace + "Folder"):
        for child in subfolder.findall(namespace + "Placemark"):
            print(child.find(namespace + "name").text)
