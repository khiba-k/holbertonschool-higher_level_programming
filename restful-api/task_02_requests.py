#!/usr/bin/python3
"""Defines function that fetches posts"""
import csv
import requests


def fetch_and_print_posts():
    """function fetches and prints"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    status = response.status_code 

    print(f"Status Code: {status}")
    if status == 200:
        data = response.json()
        
        for titles in data:
            print(titles)

    else:
        print(f"Failed to fetch data. Status code: {status}")

def fetch_and_save_posts():
    """function fetches response and saves to csv"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    status = response.status_code

    if status == 200:
        data = response.json()

        with open('posts.csv', "w", newline='') as csvf:
            field = list(data.keys())

            csv_writer = csv.DictWriter(csvf, fieldnames=field)
            csv_writer.writeheader()
            csv_writer.writerow(data)
