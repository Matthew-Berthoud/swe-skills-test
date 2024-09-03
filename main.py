import xml.etree.ElementTree as ET
import pprint
import os

def do_parse(data_dir, f):
    print("Parsing " + f)
    try:
        return ET.parse(data_dir + f) 
    except:
        print("Error while parsing, aborting")


data_dir = "Programming-Assignment-Data/"
filenames = [f[:-4] for f in os.listdir(data_dir) if f.endswith(".xml")]

for f in filenames:
    box_coords = []

    tree = do_parse(data_dir, f + ".xml")
    root = tree.getroot()
    elements = root.iter()
    for element in elements:
        # print("\n" + str(element.tag))
        # pprint.pp(element.attrib)
        is_leaf = True
        for child in element:
            is_leaf = False
            break
        if is_leaf:
            bounds = element.attrib.get("bounds")
            bounds = bounds.replace('][', '],[')
            bounds = eval(bounds)
            print(bounds)