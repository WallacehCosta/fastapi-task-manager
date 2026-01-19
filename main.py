from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from core.database import Base, engine
from routers import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Task Manager")

app.include_router(auth.router)
app.include_router(tasks.router)
