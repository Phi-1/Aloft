import json
import os

class JSON_DB:
    FILEPATH = None
    DATA = {
        "projects": {
            "testproject1": [
                "point 1",
                "point 2",
                "point 3"
            ]
        }
    }

    @staticmethod
    def save_data():
        with open(JSON_DB.FILEPATH, "w") as f:
            f.write(json.dumps(JSON_DB.DATA))

    @staticmethod
    def connect(filepath):
        JSON_DB.FILEPATH = filepath
        if os.path.exists(JSON_DB.FILEPATH):
            with open(JSON_DB.FILEPATH, "r") as f:
                JSON_DB.DATA = json.loads(f.read())
        else:
            JSON_DB.save_data()

    @staticmethod
    def add_project(title):
        JSON_DB.DATA["projects"][title] = []
        JSON_DB.save_data()
        
    @staticmethod
    def add_point(project_title, point):
        JSON_DB.DATA["projects"][project_title].append(point)
        JSON_DB.save_data()

    @staticmethod
    def get_projects():
        return JSON_DB.DATA
