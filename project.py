import json
from utils import Validator
from editproject import edit_project
from getandadd import add_project, get_projects


def create_project(useremail):
    print(" Create Project ".center(48, "*"))
    title = Validator.validate_name("Project Title")
    details = Validator.validate_name("Project Details")
    total_target = Validator.validate_number("Total Target")
    start_date = Validator.validate_time("Start Time")
    end_date = Validator.validate_time("End Time", start_date)

    new_project = {
        "Title": title,
        "Details": details,
        "Total_Target": total_target,
        "Start_Time": str(start_date),
        "End_Time": str(end_date),
        "User": useremail,
    }
    if new_project:
        add_project(new_project)
        print(" Registration Successful ".center(48, "*"))
    else:
        print(" Registration Failed ".center(48, "*"))


def view_all_project():
    print(" All Projects ".center(48, "*"))
    projects = get_projects()
    if projects:
        for project in projects:
            print(
                f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
            )
    else:
        print(" No Projects To View ".center(48, "*"))


def view_your_projects(useremail):
    print(" User Projects ".center(48, "*"))
    count = 0
    projects = get_projects()
    for project in projects:
        if project["User"] == useremail:
            print(
                f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
            )
            count += 1
    if not count:
        print(" No Projects To View ".center(48, "*"))


def update_project(useremail):
    if useremail:
        edit_project(useremail)


def delete_project(useremail):
    deleteditem = input("Enter Title Of The Project You Want To Delete\n")
    projects = get_projects()
    for project in projects:
        if useremail == project["User"] and deleteditem == project["Title"]:
            projects.remove(project)
            print("Successfully Deleted")
    try:
        with open("./projects.json", "w") as json_file:
            json.dump(projects, json_file)
    except Exception as e:
        return []
