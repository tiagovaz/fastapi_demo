from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

router = APIRouter()

# Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Index route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, session: Session = Depends(get_session)):
    todos = session.exec(select(TodoItem)).all()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

# Create todo
@app.post("/todos", response_class=HTMLResponse)
async def create_todo_form(request: Request, id: int = Form(...), title: str = Form(...)):
    with Session(engine) as session:
        todo = TodoItem(id=id, title=title)
        session.add(todo)
        session.commit()
        session.refresh(todo)
    return RedirectResponse("/", status_code=303)

# Complete todo
@app.post("/todos/{todo_id}", response_class=HTMLResponse)
async def complete_todo_form(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(TodoItem, todo_id)
    if todo:
        todo.completed = True
        session.commit()
        session.refresh(todo)
    return RedirectResponse("/", status_code=303)

