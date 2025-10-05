#!/usr/bin/python3
"""
Module: task_03_xml
===================

This module provides two main functions to handle XML serialization
and deserialization of Python dictionaries using Python’s standard
`xml.etree.ElementTree` module.

Functions:
    - serialize_to_xml(dictionary, filename)
    - deserialize_from_xml(filename)

Example:
    >>> data = {"name": "Alice", "age": 25, "is_student": True}
    >>> serialize_to_xml(data, "data.xml")
    >>> loaded_data = deserialize_from_xml("data.xml")
    >>> print(loaded_data)
    {'name': 'Alice', 'age': 25, 'is_student': True}
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save.

    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        root = ET.Element("data")

        # Add each key-value pair as a child element
        for key, value in dictionary.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        # Write XML to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict | None: A dictionary containing the XML data if successful,
                     otherwise None.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for element in root:
            text = element.text

            # Try to infer data types (bool, int, float, str)
            if text is None:
                value = None
            elif text.lower() == "true":
                value = True
            elif text.lower() == "false":
                value = False
            else:
                try:
                    # Try to convert to int or float if possible
                    if "." in text:
                        value = float(text)
                    else:
                        value = int(text)
                except ValueError:
                    value = text

            data[element.tag] = value

        return data

    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    except Exception:
        return None
