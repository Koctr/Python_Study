# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import xml.etree.cElementTree as ET

tree = ET.parse("demo.xml")
root = tree.getroot()

for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("update_by", "Koctr")

tree.write("demo_update.xml")

for country in root.findall("country"):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write("demo_remove.xml")
