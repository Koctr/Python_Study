# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import xml.etree.ElementTree as ET

tree = ET.parse("demo.xml")
root = tree.getroot()
print(root)
print(root.tag)

for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text, i.attrib)

for year in root.iter("year"):
    print(year.tag, year.text)
