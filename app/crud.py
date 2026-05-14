from sqlalchemy.orm import Session
import logging

from app import models, schemas
logger = logging.getLogger(__name__)


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()



def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()



def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    logger.info(f"Task operation successful: {db_task.id}")

    return db_task



def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = get_task(db, task_id)

    if not db_task:
        return None

    update_data = task.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    logger.info(f"Task {db_task.id} updated successfully")
    return db_task



def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return db_task