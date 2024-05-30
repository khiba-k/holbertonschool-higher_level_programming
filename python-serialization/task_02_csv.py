#!/usr/bin/python3
"""Defines function that converts csv to json"""
import csv
import json


def convert_csv_to_json(csv_file, data.json):
    """Function writes data to data.json
    Args:
        csv_file: csv file to convert
        data.json: json file to write to
    """
    data = []
    with open(csv_file, encoding="utf-8") as csvf:
        csvReader = csv.Reader(csvf)

        for rows in csvf:
            data.append(row)
