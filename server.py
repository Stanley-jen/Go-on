import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Invalid code"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway uses PORT env variable
    app.run(host="0.0.0.0", port=port)
