
#### CONTACT BOOK

contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} added successfully")


def find_contact(name):
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found")


def list_contacts():
    print("\nContacts:")

    if len(contacts) == 0:
        print("No contacts available")
        return

    for name, phone in contacts.items():
        print(name, "-", phone)



#### TO DO LIST


tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed")
    else:
        print("Task not found")


def show_tasks():

    print("\nTasks:")

    if len(tasks) == 0:
        print("No tasks available")
        return

    for index, task in enumerate(tasks, start=1):
        print(index, ".", task)


# DEMO CONTACT BOOK


add_contact("Sai", "9876543210")
add_contact("Rahul", "9123456789")

find_contact("Sai")
find_contact("Priya")

list_contacts()


# DEMO TODO LIST


add_task("Learn Python")
add_task("Practice SQL")
add_task("Build Project")

show_tasks()

remove_task("Practice SQL")

show_tasks()