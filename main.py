from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4  # used to create unique IDs for tasks

# Create a FastAPI app instance
app = FastAPI(
    title="FastAPI Task Manager",
    description="A simple API to manage your daily tasks",
    version="2.0.0"
)


# Define how a task looks using a Pydantic model
class Task(BaseModel):
    id: str                 # unique task ID (string)
    text: str               # the task description
    is_done: bool = False   # whether the task is done or not
    priority: Optional[str] = "normal"  # task priority (low, normal, high)


# Store tasks in a list (acts like a temporary in-memory database)
tasks: list[Task] = []


@app.get("/")
def root():
    # Basic welcome message at the root URL
    return {"message": "Welcome to the FastAPI Task Manager! 🚀"}


@app.post("/tasks", response_model=Task)
def create_task(text: str, priority: Optional[str] = "normal"):
    """
    Create a new task and add it to the task list.
    Each task gets a unique ID using uuid4().
    """
    task = Task(id=str(uuid4()), text=text, priority=priority)
    tasks.append(task)
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks(
    limit: int = Query(10, ge=1),          # maximum number of tasks to return
    done: Optional[bool] = None,           # optional filter: completed or not
    priority: Optional[str] = None         # optional filter: priority level
):
    """
    Return a list of tasks.
    You can filter by completion status or priority.
    """
    filtered = tasks

    # Filter tasks by "done" status if provided
    if done is not None:
        filtered = [t for t in filtered if t.is_done == done]

    # Filter tasks by priority if provided
    if priority:
        filtered = [t for t in filtered if t.priority == priority]

    # Return up to 'limit' number of tasks
    return filtered[:limit]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    """
    Get a single task by its ID.
    If not found, return a 404 error.
    """
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, text: Optional[str] = None, is_done: Optional[bool] = None):
    """
    Update a task's text or completion status.
    Only updates provided fields (text or is_done).
    """
    for task in tasks:
        if task.id == task_id:
            if text is not None:
                task.text = text
            if is_done is not None:
                task.is_done = is_done
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    """
    Delete a task from the list by its ID.
    """
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"detail": f"Task {task_id} deleted successfully"}
