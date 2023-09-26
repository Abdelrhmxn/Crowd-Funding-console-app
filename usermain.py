import os
import project


def secondaryMenu(useremail, fname):
    os.system("clear")
    print(f" WELCOME {fname} ".center(48, "*"))
    active_user = useremail
    while True:
        choice = input(
            "Choose:\n 1)Create Project\n 2)View All Projects\n 3)View Your Project\n 4)Updata Your Project\n 5)Delete Your Project\n 6)Exit\n"
        )
        if choice.isnumeric():
            choice = int(choice)
        if choice == 1:
            project.create_project(active_user)
        elif choice == 2:
            project.view_all_project()
        elif choice == 3:
            project.view_your_projects(active_user)
        elif choice == 4:
            project.update_project(active_user)
        elif choice == 5:
            project.delete_project(active_user)
        elif choice == 6:
            exit()
