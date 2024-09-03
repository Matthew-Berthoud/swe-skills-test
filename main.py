import os
import sys
import pprint
import xml.etree.ElementTree as ET

def do_parse(data_dir, f):
    print("Parsing " + f)
    try:
        if data_dir[-1] != "/":
            data_dir = data_dir + "/"
        return ET.parse(data_dir + f) 
    except:
        print("Error while parsing, aborting")

argc = len(sys.argv)
if argc != 2:
    print("Usage: python3 main.py PATH_TO_DATA_DIR")
    exit(0)

data_dir = sys.argv[1]
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