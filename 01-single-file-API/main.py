# Import necessary modules from FastAPI and Pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create an instance of the FastAPI application
app = FastAPI(title="FastAPI To-Do App")

# In-memory database to store to-do items
todo_db = []

# Define the data model for a to-do item using Pydantic
# Using type annotations for pydantic, so data is validated, serialized and
# fastapi will generate proper documentation
class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

# Endpoint to list all to-do items
@app.get("/todos", response_model=List[TodoItem])
def list_todos():
    return todo_db  # Return the list of all to-do items

# Endpoint to create a new to-do item
@app.post("/todos", response_model=TodoItem)
def create_todo(item: TodoItem):
    todo_db.append(item)
    return item

# Endpoint to mark a to-do item as completed
@app.put("/todos/{todo_id}", response_model=TodoItem)
def complete_todo(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            todo.completed = True
            return todo
    # If the item is not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Todo not found")
