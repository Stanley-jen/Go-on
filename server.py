import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example "database" of license codes
LICENSES = {
    "TEST123": {"status": "active"},
    "EXPIRED1": {"status": "expired"}
}

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if not code:
        return jsonify({"status": "error", "message": "No code provided"}), 400

    license_info = LICENSES.get(code)
    if license_info:
        if license_info["status"] == "active":
            return jsonify({"status": "success", "message": "License valid"})
        else:
            return jsonify({"status": "error", "message": "Subscription expired"})
    return jsonify({"status": "error", "message": "Invalid license code"})


if __name__ == "__main__":
    # Get the PORT Railway assigns, default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Listen on all interfaces
    app.run(host="0.0.0.0", port=port)
