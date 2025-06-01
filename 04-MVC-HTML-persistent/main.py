from fastapi import FastAPI, HTTPException, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, create_engine, Session, select
from typing import Optional
from models.todo import TodoItem
from controllers.todo_controller import router as todo_router
from database import on_startup

app = FastAPI(title="FastAPI To-Do App")
app.include_router(todo_router)

@app.on_event("startup")
def startup_event():
    on_startup()

