tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} removed")
    else:
        print("Task not found")

def show_tasks():

    print("\n Tasks:")

    if len(tasks) == 0:
        print(" No tasks available")
        return
    
    for index,task in enumerate(tasks, start=1):
        print(index, ".", task)