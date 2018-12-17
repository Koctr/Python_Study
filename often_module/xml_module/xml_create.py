# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import xml.etree.cElementTree as ET

demo_create = ET.Element("papa")
name = ET.SubElement(demo_create, "TianYuehua", attrib={'bobo': 'E'})
age = ET.SubElement(name, "age")
age.text = '36'

name2 = ET.SubElement(demo_create, "ZhouZhengshu", attrib={'bobo': 'B'})
age = ET.SubElement(name2, "age")
age.text = '22'

name3 = ET.SubElement(demo_create, "HanYan", attrib={'bobo': 'B-'})
age = ET.SubElement(name3, "age")
age.text = '22'

file = ET.ElementTree(demo_create)
file.write("demo_create.xml", encoding="utf-8", xml_declaration=True)

ET.dump(file)
