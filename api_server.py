from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "active",
        "service": "OrderService",
        "version": "2.0 - Docker Edition"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
