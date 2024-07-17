#!/usr/bin/python3
import json

def read(filename):
     with open(filename, "r") as file:
        data = json.load(file)
        values = data.get("items", [])
        return values