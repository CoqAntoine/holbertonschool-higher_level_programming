#!/usr/bin/python3
"""
A Flask RESTful API with Basic Auth.

JWT Auth, and role-based access.
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# --- Users stored in memory ---
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication setup ---
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication."""
    if username in users and check_password_hash(
            users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"})


# --- JWT Configuration ---
app.config["JWT_SECRET_KEY"] = "ton_secret_ultra_long_et_securise"
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and return a JWT access token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(
            users[username]['password'], password):
        token = create_access_token(identity={
            "username": username,
            "role": users[username]['role']
        })
        return jsonify(access_token=token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route accessible only with a valid JWT token."""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Protected route accessible only to admin users."""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# --- JWT Error Handlers ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle malformed JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token requirement errors."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    """Run the Flask API server."""
    app.run(debug=True)
