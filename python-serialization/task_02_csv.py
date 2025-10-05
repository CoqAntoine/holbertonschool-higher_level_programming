#!/usr/bin/python3
"""
Module: task_02_csv
===================

This module provides a function to convert data from a CSV file
into a JSON file named `data.json`.

It uses Python’s built-in `csv` and `json` modules.
Each row in the CSV file is converted into a dictionary
and then serialized as JSON.

Example:
    >>> convert_csv_to_json("data.csv")
    True
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name or path of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful, False otherwise.

    Process:
        1. Open the CSV file and read its content using csv.DictReader().
        2. Convert the rows into a list of dictionaries.
        3. Serialize the list into JSON format.
        4. Write the JSON data to 'data.json'.

    Exceptions:
        Returns False if the CSV file does not exist or another error occurs.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
