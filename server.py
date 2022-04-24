from flask import Flask, request, redirect
from flask_cors import CORS
from dotenv import load_dotenv
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
    load_dotenv()
    SERVER_IP = os.environ.get("SERVER_IP")
    SERVER_PORT = os.environ.get("SERVER_PORT")
    db.connect(DB_PATH)
    SERVER.run(host=SERVER_IP, port=SERVER_PORT)