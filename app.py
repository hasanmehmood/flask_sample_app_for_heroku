from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_sample_data", methods=["GET"])
def get_sample_data():
    return {"test": True, "sample_data": {"data": 1, "message": "Hello World!"}}


@app.route("/receive_data", methods=["POST"])
def receive_data():
    print(request.get_json())
    return {"success": True}
