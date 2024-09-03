# Software Engineering Skills Test and Survey
CSCI 535 Software Engineering: Homework 1

## How to run
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

## Libraries
* `os`: listing directory contents
* `sys`: taking command-line arguments
* `pprint`: more human-readable debug printing of json-ish objects
* `xml.etree.ElementTree`: parsing xml into python objects
