# from fastapi import Depends, HTTPException
# from sqlalchemy.orm import Session
#
# from app import schemas, crud
# from app.database import get_db
# # from main import app
#
#
# @app.post("/users/register/", response_model=schemas.User)
# def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)