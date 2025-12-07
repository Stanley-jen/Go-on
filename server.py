# server.py (Production Ready)
from flask import Flask, request, jsonify
# os import is no longer strictly needed but fine to leave
import os 

app = Flask(__name__)

@app.route("/")
def index():
    return "License Server is Running", 200

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success", "code": code})
    return jsonify({"status": "error", "code": code})
# File ends here. Gunicorn runs the app from Procfile.
