from fastapi import APIRouter, HTTPException, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from typing import Optional
from models.todo import TodoItem
from database import get_session

router = APIRouter()

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Index route
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, session: Session = Depends(get_session)):
    todos = session.exec(select(TodoItem)).all()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

# Create todo
@router.post("/todos", response_class=HTMLResponse)
# Required ID:
async def create_todo_form(request: Request, id: int = Form(...), title: str = Form(...), session: Session = Depends(get_session)):
# Optional ID (for auto-increment):
#async def create_todo_form(request: Request, title: str = Form(...)):
    # If we want an ID to be entered:
    todo = TodoItem(id=id, title=title)
    # If we want auto-increment:
    #todo = TodoItem(title=title)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return RedirectResponse("/", status_code=303)

# Complete todo
@router.post("/todos/{todo_id}", response_class=HTMLResponse)
async def complete_todo_form(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(TodoItem, todo_id)
    if todo:
        todo.completed = True
        session.commit()
        session.refresh(todo)
    return RedirectResponse("/", status_code=303)

