import xml.etree.ElementTree as element_tree


def get_caches(xml):
    tree = element_tree.fromstring(xml)
    for child in tree.iter('*'):
        print(child.tag)
