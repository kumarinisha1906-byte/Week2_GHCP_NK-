# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework that allows clients to create, read, update, and delete (CRUD) resources.

Students will learn how to define request/response models, use HTTP methods correctly, validate input, and persist data between restarts.

## 📝 Tasks

### 🛠️	Task 1: Set Up FastAPI Application

#### Description
Install FastAPI and create a basic application with a root endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a FastAPI application instance
- Define a GET endpoint at `/` that returns a JSON welcome message
- Include clear code comments explaining each part of the app

### 🛠️	Task 2: Implement CRUD Operations

#### Description
Add endpoints to manage a collection of tasks (or books) using proper HTTP methods.

#### Requirements
Completed program should:

- Use Pydantic models to define request/response schemas
- Implement CRUD endpoints:
  - `GET /tasks` or `GET /books` (list all items)
  - `POST /tasks` or `POST /books` (create a new item)
  - `PUT /tasks/{id}` or `PUT /books/{id}` (update an existing item)
  - `DELETE /tasks/{id}` or `DELETE /books/{id}` (delete an item)
- Use appropriate HTTP status codes
- Validate input and return meaningful error messages

### 🛠️	Task 3: Add Data Persistence

#### Description
Ensure the API persists data between server restarts using a simple file-based store.

#### Requirements
Completed program should:

- Store items in a JSON file (e.g., `tasks.json` or `books.json`)
- Load existing data when the app starts
- Save data after each create/update/delete operation
- Handle file I/O errors gracefully


---

### 📦 Starter Code

Use the included `starter-code.py` file as a starting point. It contains the FastAPI app setup and initial data models.
