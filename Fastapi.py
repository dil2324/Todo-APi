
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

# ----- МОДЕЛЬ -----
class Task(BaseModel):
    id: int
    title: str
    done: bool = False
class TaskResponse(BaseModel):
    message: str
    task: Optional[Task] = None

tasks: list[Task] = []

# ----- GET все задачи -----
@app.get("/tasks")
def get_tasks()-> list[Task]:
    return tasks


# ----- GET одна задача -----
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# ----- POST создать задачу -----
@app.post("/tasks")
def create_task(task: Task):
    for existing_task in tasks:
        if existing_task.id == task.id:
            raise HTTPException(
            status_code=409,
            detail="Task with this id already exists"
        )
    tasks.append(task)
    return TaskResponse(message="Task created", task=task)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task

            return TaskResponse(
                message="Task updated",
                task=updated_task
            )

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
    
    
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return TaskResponse(message="Task deleted", task=task)
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )