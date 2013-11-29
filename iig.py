#!/usr/bin/python3

"""this is process to generate index.html with images."""

from os import walk
import re

try:
    #list files in directory recursively
    files = []
    for dirpath, dirnames, filenames in walk('images'):
        for filename in filenames:
            files.append("%s/%s" % (dirpath, filename))

    #filter only image files
    files = [i for i in files if re.match(".*(png|jpeg|jpg)$", i)]

except:
    print("images directory not exist")
    import sys
    sys.exit(1)

from jinja2 import Template
template = Template(open("template.html", "r").read())

open("index.html", "w").write(template.render(images=files))
