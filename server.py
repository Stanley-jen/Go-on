from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success", "code": code})
    return jsonify({"status": "error", "code": code})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
