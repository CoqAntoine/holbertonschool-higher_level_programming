#!/usr/bin/python3
"""A simple RESTful API built 
with Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
}


@app.route('/')
def home():
    """Root endpoint of the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Returns a list of all usernames in the API."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """Endpoint to check the API's status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Retrieves information about a specific user."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the in-memory users dictionary."""
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    users[username] = data  # Ajoute le nouvel utilisateur
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
