from fastapi import FastAPI
from models.todo import TodoItem
from controllers.todo_controller import router as todo_router
from database import on_startup

app = FastAPI(title="FastAPI To-Do App")
app.include_router(todo_router)

@app.on_event("startup")
def startup_event():
    on_startup()
