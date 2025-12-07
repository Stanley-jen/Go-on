from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_LICENSES = {"TEST123": True, "USERABC": True}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    key = data.get("license_key")
    return jsonify({"valid": VALID_LICENSES.get(key, False)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
