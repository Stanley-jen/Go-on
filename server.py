from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/validate", methods=["GET"])
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
