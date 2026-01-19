from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.task import TaskCreate, TaskResponse
from services.task_service import create_task, get_tasks_by_user, delete_task
from routers.deps import get_current_user
from models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_task(db, task.title, user.id)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_tasks_by_user(db, user.id)


@router.delete("/{task_id}")
def remove(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    delete_task(db, task_id, user.id)
    return {"message": "Tarefa removida"}
