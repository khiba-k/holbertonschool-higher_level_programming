#!/usr/bin/python3
import json
import csv

def read(filename):
     with open(filename, "r") as file:
        data = json.load(file)
        values = data.get("items", [])
        return values
     
def read_json():
    with open('products.json') as f:
        products = json.load(f)
    return products

def read_csv():
    products = []
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append({
				"id": int(row['id']),
				"name": row['name'],
				"category": row['category'],
				"price": float(row['price'])
            })