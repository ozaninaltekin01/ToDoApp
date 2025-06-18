from fastapi import FastAPI
from models import Base
from database import engine
from routers.auth import router as auth_routher
from routers.todo import router as todo_router

app = FastAPI()
app.include_router(auth_routher, prefix="/auth", tags=["Auth"])
app.include_router(todo_router, prefix="/todo", tags=["Todo"])

Base.metadata.create_all(bind=engine)


