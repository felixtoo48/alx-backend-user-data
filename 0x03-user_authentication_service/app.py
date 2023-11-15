#!/usr/bin/env python3
""" Flask App """

from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def message() -> str:
    """ print message given """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """function to implement POST /users route """
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)

        return jsonify({"email": user.email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """ implementing login function """
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        log = AUTH.valid_login(email, password)
        if log:
            session = AUTH.create_session(session_id)
            return jsonify({"email": user.email, "message": "logged in"}), 200
    except Exception:
        return abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
