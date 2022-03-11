from flask import Flask, request

server = Flask(__name__)

def read_html(filepath):
    html = ""
    with open(filepath) as f:
        html = f.read()

    return html

@server.route("/", methods=["GET"])
def index():
    return read_html("./index.html")

@server.route("/", methods=["POST"])
def add_project():
    return request.form["name"]

if __name__ == "__main__":
    server.run(host="localhost", port=8008)