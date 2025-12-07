# server.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# --- ADD THIS NEW ROOT ROUTE ---
@app.route("/")
def index():
    # Railway's health check will hit this route
    return "License Server is Running", 200
# -------------------------------

# Example license validation route
@app.route("/validate")
def validate():
    # ... (rest of your validation logic)
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success", "code": code})
    return jsonify({"status": "error", "code": code})

# Run the app using Railway's PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
