from src.models.models import db
from fastapi import Depends
from sqlalchemy.orm import sessionmaker, Session
from src.models.models import User
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM


def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def verify_token(token, session = Depends(get_session)):
    dic_inf = jwt.decode(toke, SECRET_KEY, ALGORITHM)
    user = session.query(User).filter(User.id==6).first()
    return user
