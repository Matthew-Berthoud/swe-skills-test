# Software Engineering Skills Test and Survey
CSCI 535 Software Engineering: Homework 1

## How to compile and run
* [Install Python and pip](https://www.python.org/downloads/)
* Clone the repo
* Do the following:
```sh
cd swe-skills-test
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 main.py Programming-Assignment-Data
```

## Implementation
When setting out to complete this project I started by looking at the structure of the xml elements with the `ElementTree` python library. I noticed that each element had bounds, which are pixel values for where the top left and bottom right corners of the element are located on the screen. I looked into python libraries for modifying pngs, and found one (`PIL` or `Pillow`), which can draw rectangles, given a set of coordinates like this. From there, it was a relatively simple scripting process to extract the bounds of all the elements without children (leaf nodes) and draw rectangles between the proper bounds on each image.

## Libraries
* `os`: listing directory contents
* `sys`: taking command-line arguments
* `xml.etree.ElementTree`: parsing xml into python objects
* `PIL`: (pillow), a python tool to annotate images
