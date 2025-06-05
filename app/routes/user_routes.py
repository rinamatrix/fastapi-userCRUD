from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.schemas.user_schema import *
from app.controllers import user_controller

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.register_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return user_controller.login_user(db, user.email, user.password)

@router.put("/profile", response_model=UserOut)
def update(user: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return user_controller.update_user(db, current_user.id, user)

@router.delete("/user")
def delete_user(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return user_controller.soft_delete_user(db, current_user.id)
