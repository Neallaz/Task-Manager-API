from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[schemas.TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@router.post("/", response_model=schemas.TaskResponse)
def create_new_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)


@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_single_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_single_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    updated_task = crud.update_task(db, task_id, task)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated_task


@router.delete("/{task_id}")
def delete_single_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}