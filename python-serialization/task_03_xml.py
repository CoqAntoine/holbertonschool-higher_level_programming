#!/usr/bin/python3
'''
task_03xml.py
File that add two function that serialized and deserialized a python
dictionary'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''Function that serialize a python dictionary into a xml file

    Args:
    dictionary: Python dictionary
    filename: Xml file you want to put the converted dictionary

    return: None'''
    root = ET.Element("data")
    for i in dictionary:
        ET.SubElement(root, i).text = dictionary[i]

    xml_dict = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        xml_dict.write(xml_file, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    '''Function that deserialized XML File, particullary dictionary, into a
    python object

    Args:
    filename: The XML file name to deserialized

    Return: the python dictionary'''
    tree = ET.parse(filename)
    root = tree.getroot()
    py_dict = {}
    for i in root:
        py_dict[i.tag] = i.text
    return py_dict
