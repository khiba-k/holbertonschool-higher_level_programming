#!/usr/bin/python3
""""""
from flask import Flask


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return("Welcome to the flask API")

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return("OK")

@app.route("/users/<username>")
def users(username):
    return(f"Hello {username}")

@app.route("/add_user")
def add_user():
    user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    return (user)

if __name__ == "__main__":
    app.run()
