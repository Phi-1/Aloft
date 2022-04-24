from flask import Flask, request, redirect
from flask_cors import CORS
from src.json_db import JSON_DB as db
import os

SERVER = Flask(__name__)
CORS(SERVER)
DB_PATH = os.path.abspath("./projects.json")

def read_html(filepath):
    with open(filepath) as f:
        return f.read()

@SERVER.route("/", methods=["GET"])
def index():
    return read_html("./index.html")

@SERVER.route("/add-project", methods=["POST"])
def add_project():
    db.add_project(request.form["name"])
    return redirect("/")

@SERVER.route("/get-projects", methods=["GET"])
def get_projects():
    return db.get_projects()

@SERVER.route("/add-point", methods=["POST"])
def add_point():
    db.add_point(request.form["new-point"])
    return redirect("/")
    

if __name__ == "__main__":
    db.connect(DB_PATH)
    SERVER.run(host="192.168.11.43", port=7232)