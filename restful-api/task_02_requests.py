#!/usr/bin/python3
"""Defines function that fetches posts"""
import json
import requests


def fetch_and_print_posts():
    """function fetches and prints"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    status = response.status.code 

    print(f"Status Code: {status}")
    if response.status.code == 200:
        data = response.json()
        
        for titles in data:
            print("{titles}")

def fetch_and_save_posts():
    """function fetches and saves posts"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    status = response.status.code

    if response.status.code == 200:
        data = response.json
        
        with open("posts.csv", "w") as file:
            writer = csv.write(file)

            for item in data:
                writer.writerow([item])

