from project import Project
import csv
import datetime

def main():
    with open('projects.txt') as csv_file:
        csv_reader = list(csv.reader(csv_file))

    csv_file.close()

    print_menu()

    input_menu = input(">>> ")

    loop = True

    while loop:
        if input_menu.upper() == "D":
            display_projects(csv_reader)
            input_menu = ""
        if input_menu.upper() == "U":
            update_project(csv_reader)
            input_menu = ""
        if input_menu.upper() == "A":
            add_project(csv_reader)
            input_menu = ""
        if input_menu.upper() == "F":
            filter_by_date(csv_reader)
            input_menu = ""
        if input_menu.upper() == "S":
            save(csv_reader)
            input_menu = ""
        if input_menu.upper() == "Q":
            save(csv_reader)
            loop = False
        else:
            print_menu()
            input_menu = input(">>> ")

def save(csv_reader):
    open('projects.txt', 'w').close()
    with open('projects.txt', 'w') as f:
        for projects in csv_reader:
            print(f"{projects[0].split("\t")[0]}\t{projects[0].split("\t")[1]}\t{projects[0].split("\t")[2]}\t{projects[0].split("\t")[3]}\t{projects[0].split("\t")[4]}", file=f)
    f.close()

def filter_by_date(csv_reader):
    input_date = filter_date()
    for row in csv_reader:
        if csv_reader.index(row) > 0:
            if row[0].split("\t")[1] == input_date:
                project = Project(row[0].split("\t")[0], row[0].split("\t")[1], row[0].split("\t")[2],
                                  row[0].split("\t")[3], row[0].split("\t")[4])
                print(project)


def add_project(csv_reader):
    input_name = filter_name()
    input_date = filter_date()
    input_priority = update_priority_function()
    input_cost = filter_cost_estimate()
    input_percentage = filter_percentage_update(csv_reader)

    csv_reader.append([input_name + "\t" + input_date + "\t" + input_priority + "\t" + input_cost + "\t" + input_percentage])

def filter_cost_estimate():
    input_cost = input("Cost estimate:")  # e.g., "30/9/2022"
    bool = True
    while bool:
        try:
            if float(input_cost) < 1:
                print(f"Input Cannot be 0")
                input_cost = input("Date (d/m/yyyy): ")
            else:
                bool = False
        except ValueError:
            print("Wrong Cost Input")
            input_cost = ""

    return input_cost

def filter_date():
    input_date = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    bool = True
    try:
        date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
    except ValueError:
        print("Error Wrong Date Input")
        input_date = ""
    while bool:
        try:
            if str(input_date) == "":
                print(f"String cannnot be empty")
                input_date = input("Date (d/m/yyyy): ")
                date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
            else:
                bool = False
        except ValueError:
            print("Wrong Date")
            input_date = ""

    return date.strftime("%d/%m/%Y")

def filter_name():
    input_name = input("Name: ")
    bool = True
    while bool:
        if str(input_name) == "":
            print(f"String cannnot be empty")
            input_name = input("Name: ")
        else:
            bool = False

    return input_name

def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project ")
    print("- (U)pdate project")
    print("- (Q)uit")

def display_projects(csv_reader):
    completed_projects = []
    for row in csv_reader:
        if csv_reader.index(row) > 0:
            if int(row[0].split("\t")[4]) >= 100:
                project = Project(row[0].split("\t")[0], row[0].split("\t")[1], row[0].split("\t")[2],
                                  row[0].split("\t")[3], row[0].split("\t")[4])
                completed_projects.append(project)
            else:
                project = Project(row[0].split("\t")[0], row[0].split("\t")[1], row[0].split("\t")[2],
                                      row[0].split("\t")[3], row[0].split("\t")[4])
                print(f"{csv_reader.index(row)}. {project}")

    print("Completed Projects: ")
    for projects in completed_projects:
        print(projects)

def filter_percentage_update(csv_reader):
    input_update_choice = input("New Percentage: ")
    bool = True
    while bool:
        try:
            if int(input_update_choice) < 1 or int(input_update_choice) > 100:
                print(f"Enter Number between 1% and 100%")
                input_update_choice = input("Project Choice: ")
            else:
                bool = False
        except ValueError:
            print("Invalid Input")
            input_update_choice = 0

    return input_update_choice

def filter_update_input(csv_reader):
    input_update_choice = input("Project Choice: ")
    bool = True
    while bool:
        try:
            if int(input_update_choice) < 1 or int(input_update_choice) > len(csv_reader) - 1:
                print(f"Enter Number between 1 and {len(csv_reader) - 1}")
                input_update_choice = input("Project Choice: ")
            else:
                bool = False
        except ValueError:
            print("Invalid Input")
            input_update_choice = 0

    return input_update_choice

def update_priority_function():
    input_update_choice = input("Priority: ")
    bool = True
    while bool:
        try:
            if int(input_update_choice) < 1 or int(input_update_choice) > 10:
                print(f"Enter Number between 1 and 10")
                input_update_choice = input("Priority: ")
            else:
                bool = False
        except ValueError:
            print("Invalid Input")
            input_update_choice = 0

    return input_update_choice

def update_project(csv_reader):
    display_projects(csv_reader)

    update_index = int(filter_update_input(csv_reader))
    update_percentage = str(filter_percentage_update(csv_reader))
    update_priority = update_priority_function()

    length_of_suffix_percentaqe = len(csv_reader[update_index][0].split("\t")[4])
    length_of_suffix_estimate = len(csv_reader[update_index][0].split("\t")[3])
    length_of_suffix_priority = len(csv_reader[update_index][0].split("\t")[2])
    csv_reader[update_index][0] = csv_reader[update_index][0][0:-length_of_suffix_percentaqe - length_of_suffix_estimate - length_of_suffix_priority - 3] + "\t" + str(update_priority) + "\t" + str(csv_reader[update_index][0].split("\t")[3] + "\t") + str(update_percentage)
    print(csv_reader[update_index][0])


main()