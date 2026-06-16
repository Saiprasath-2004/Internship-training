from fastapi import FastAPI, HTTPException
from models import Task
from data import tasks

app= FastAPI()


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/task/{id}")
def get_task_by_id(id: int):
    for task in tasks:
        if task.id == id:
            return task
    

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.put("/task/{id}")
def update_task(id: int,task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks[i]=task
            return task
        
    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )

@app.delete("/tasks/{id}")
def delete_task(id:int):
    for i  in range(len(tasks)):
        if tasks[i].id == id:
            del tasks[i]
            return "Deleted Successfully"
    
    raise HTTPException(
        status_code=404,
        detail="task not found"
    )