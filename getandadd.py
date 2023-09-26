import json


def add_project(new_project):
    try:
        listprojects = get_projects()
        with open("./projects.json", "w") as json_file:
            listprojects.append(new_project)
            json.dump(listprojects, json_file)
    except Exception as e:
        print(e)


def get_projects():
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            return projects
    except Exception as e:
        return []


def get_project(title, email):
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            for project in projects:
                if project["Title"] == title and project["User"] == email:
                    return project
    except Exception as e:
        print(e)


def get_project(title, email):
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            for project in projects:
                if project["Title"] == title and project["User"] == email:
                    return project
    except Exception as e:
        print("*" * 48)
