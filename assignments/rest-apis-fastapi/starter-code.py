# Starter code for Building REST APIs with FastAPI

# Install required packages:
# pip install fastapi uvicorn pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(
    title="Task Management API",
    description="A simple task management system built with FastAPI"
)

# Data model for a Task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Data models for a Book resource
class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None

# In-memory storage (will be replaced with file storage in Task 3)
tasks: List[Task] = []
next_id = 1

# File path for data persistence
DATA_FILE = "tasks.json"

@app.get("/")
async def root():
    return {"message": "Welcome to the Task Management API"}

# TODO: Task 2 - Implement CRUD Operations
# Add endpoints for:
# - GET /tasks (get all tasks)
# - POST /tasks (create new task)
# - PUT /tasks/{task_id} (update task)
# - DELETE /tasks/{task_id} (delete task)

# TODO: Task 3 - Add Data Persistence
# - Load tasks from JSON file on startup
# - Save tasks to JSON file after each operation
