#!/usr/bin/python3
"""Flask API with Basic Auth, JWT Auth, and role-based access."""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials."""
    if username in users and check_password_hash(
            users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protect Auth route."""
    return jsonify({"message": "Basic Auth: Access Granted"})


app.config["JWT_SECRET_KEY"] = "ton_secret_ultra_long_et_securise"
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    """Login and return JWT token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and check_password_hash(
            users[username]['password'], password):
        token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify(access_token=token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected route."""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route."""
    claims = get_jwt()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True)
