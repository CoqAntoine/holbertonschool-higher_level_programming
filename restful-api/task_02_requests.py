#!/usr/bin/python3
"""
This script fetches posts from the JSONPlaceholder API, prints their titles,
and saves the data into a CSV file.
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetch posts from the JSONPlaceholder API and print their titles.

    Makes an HTTP GET request to:
        https://jsonplaceholder.typicode.com/posts

    Prints:
        - The HTTP status code of the request.
        - The title of each post if the request succeeds (status code 200).

    Returns:
        None
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status code: {r.status_code}")

    if r.status_code == 200:
        r_json = r.json()
        for i in r_json:
            print(i['title'])

def fetch_and_save_posts():
    """
   Fetch posts from the JSONPlaceholder API and save them into a CSV file.

    Makes an HTTP GET request to:
        https://jsonplaceholder.typicode.com/posts

    If the request is successful (status code 200), extracts for each post:
        - id
        - title
        - body

    The data is then written to a CSV file named "posts.csv"
    with the columns: ['id', 'title', 'body'].

    Returns:
        csv_file (TextIOWrapper): The CSV file object after writing.
        None: If the request fails.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        r_json = r.json()
        dict_list = []
        for i in r_json:
            new_dict = {}
            new_dict['id'] = i['id']
            new_dict['title'] = i['title']
            new_dict['body'] = i['body']
            dict_list.append(new_dict)
        fields = ['id', 'title', 'body']
        with open("posts.csv", "w") as csv_file:
            write_dict = csv.DictWriter(csv_file, fieldnames=fields)
            write_dict.writeheader()
            write_dict.writerows(dict_list)
        return csv_file
