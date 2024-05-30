#!/usr/bin/python3
"""Defines function that converts csv to json"""
import csv
import json


def convert_csv_to_json(csv_file):
    """Function writes data to data.json
    Args:
        csv_file: csv file to convert
        data.json: json file to write to
    """

    data = []
    try:
        with open(csv_file, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                data.append(row)

    except FileNotFoundError:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except:
        return False
    return True
