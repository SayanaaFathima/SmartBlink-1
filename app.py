from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/blink", methods=["POST"])
def receive_blink():
    data = request.get_json()
    count = data.get("count", 0)
    print(f"Received blink count: {count}")
    # You can store this in a file or database if needed
    return jsonify({"status": "received", "count": count})

if __name__ == "__main__":
    app.run(debug=True)