import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

argc = len(sys.argv)
if argc != 2:
    print("Usage: python3 main.py PATH_TO_DATA_DIR")
    exit(0)

data_dir = sys.argv[1]
filenames = [f[:-4] for f in os.listdir(data_dir) if f.endswith(".xml")]

for f in filenames:
    print("Parsing " + f)
    if data_dir[-1] != "/":
        data_dir = data_dir + "/"
    try:
        tree = ET.parse(data_dir + f + ".xml") 
    except:
        print(f"Failed to parse {f}, aborting")
        continue

    box_coords = []
    root = tree.getroot()
    elements = root.iter()
    for element in elements:
        is_leaf = True
        for child in element:
            is_leaf = False
            break
        if not is_leaf:
            continue

        bounds = element.attrib.get("bounds", "[0,0][0,0]")
        bounds = bounds.replace('][', ',')
        bounds = eval(bounds)
        box_coords.append(bounds)
    
    with Image.open(data_dir + f + ".png") as im:
        draw = ImageDraw.Draw(im)
        for coords in box_coords:
            draw.rectangle(xy=coords, outline="yellow", width=8)
        im.save("output/" + f + ".png", "PNG")
