import xml.etree.ElementTree as ET
import os

def do_parse(data_dir, f):
    print("Parsing " + f)
    try:
        ET.parse(data_dir + f) 
    except:
        print("Error while parsing, aborting")


data_dir = "Programming-Assignment-Data/"
trees = [do_parse(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".xml")]
