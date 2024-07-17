#!/usr/bin/python3
import json
import csv
import sqlite3

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

def read_db():
    products = []
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    product = cursor.fetchall()
    conn.close()
    for row in product:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products