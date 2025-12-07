from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/validate")
def validate():
    code = request.args.get("code")
    if code == "TEST123":
        return jsonify({"status": "success", "code": code})
    else:
        return jsonify({"status": "error", "message": "Subscription expired"})

# Only for local testing
if __name__ == "__main__":
    app.run()
