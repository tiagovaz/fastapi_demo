from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel

app = FastAPI(title="FastAPI To-Do App")

# In-memory database to store to-do items
todo_db = []

# Define the data model for a to-do item
# We don't really need pydantic here, as we don't need serialization, we're
# just rendering HTML
class TodoItem:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

# ...but we can keep using pydantic as well
#class TodoItem(BaseModel):
#    id: int
#    title: str
#    completed: bool = False

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Index router
# async will assure non-blocking operations
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todo_db})


# Form(...) tells FastAPI to extract this value from an HTML form.
# The ... inside it means required
@app.post("/todos", response_class=HTMLResponse)
# type hints will enforce validation even for non-pydantic objects
async def create_todo_form(request: Request, id: int = Form(...), title: str = Form(...)):
    item = TodoItem(id=id, title=title)
    todo_db.append(item)
    return RedirectResponse("/", status_code=303)

# Update todo item
@app.post("/todos/{todo_id}", response_class=HTMLResponse)
async def complete_todo_form(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            todo.completed = True
            break
    return RedirectResponse("/", status_code=303)
