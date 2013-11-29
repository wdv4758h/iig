#!/usr/bin/python3

"""this is process to generate index.html with images."""

from os import getcwd, walk
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

pwd = getcwd()

webpage = "<head>\n"
webpage += "<title>Generated Image Page</title>\n"
webpage += """<style type="text/css">
                img {
                    height: auto;
                    width: auto;
                    max-width: 100%;
                }
                </style>\n"""
webpage += "</head>\n"

for i in files:
    webpage += "<div><img src=\"%s/%s\" /></div>\n<br/>\n" % (pwd, i)

open("index.html", "w").write(webpage)
