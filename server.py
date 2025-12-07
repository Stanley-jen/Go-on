from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success", "code": code})
    return jsonify({"status": "error", "code": code})

# Optional: default route to show server is alive
@app.route("/")
def home():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    # Port is ignored by Railway when using Gunicorn
    app.run(host="0.0.0.0", port=8080)
