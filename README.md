#  FastAPI Task Manager

 A clean and modern **Task Manager API** built with [FastAPI](https://fastapi.tiangolo.com/).  
 Create, view, update, delete, and filter tasks — all through a simple REST API with beautiful interactive docs.

---

##  Features

 Create tasks with custom priority (`low`, `normal`, `high`)  
 List and filter tasks by completion or priority  
 Update task text or mark as done/undone  
 Delete tasks easily  
 Interactive Swagger UI at `/docs`  
 Super-fast and type-safe with **FastAPI + Pydantic**

---

##  Tech Stack

| Component | Purpose |
|------------|----------|
|  **Python 3.10+** | Programming language |
|  **FastAPI** | Web framework |
|  **Pydantic** | Data validation and models |
|  **Uvicorn** | ASGI server for running the app |

---

##  Getting Started

### 1. Clone the Repository

git clone https://github.com/andrews.botchway/fastapi-task-manager.git
cd fastapi-task-manager

### 2. Install Dependencies
pip install fastapi uvicorn

### 3. Run the App
uvicorn main:app --reload

### 4. Open in Browser

 Docs (Swagger UI): http://127.0.0.1:8000/docs

 Docs (ReDoc): http://127.0.0.1:8000/redoc

 Root Endpoint: http://127.0.0.1:8000/

--- 


###  API Endpoints
| Method | Endpoint           | Description |
|--------|--------------------|-------------|
| GET    | `/`                | Welcome message |
| POST   | `/tasks`           | Create a new task |
| GET    | `/tasks`           | List all tasks (with filters) |
| GET    | `/tasks/{task_id}` | Retrieve a single task |
| PUT    | `/tasks/{task_id}` | Update a task’s text or completion status |
| DELETE | `/tasks/{task_id}` | Delete a task |
---

###  Example Usage (via curl)
- Create a Task
curl -X POST "http://127.0.0.1:8000/tasks?text=Buy milk&priority=high"

- Mark Task as Done
curl -X PUT "http://127.0.0.1:8000/tasks/<task_id>?is_done=true"

- Delete a Task
curl -X DELETE "http://127.0.0.1:8000/tasks/<task_id>"

