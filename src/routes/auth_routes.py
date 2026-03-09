from fastapi import APIRouter, Depends, HTTPException
from src.models.models import User
from src.dependencies.dependencies import get_session, verify_token
from src.main import bcrypt_context, ACCESS_TOKEN_EXPIRE__MINUTES, ALGORITHM, SECRET_KEY
from src.schemas.schemas import UserSchema, LoginSchema
from sqlalchemy.orm import session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=['auth'] )

def create_token(id_user, token_duration = timedelta(minutes=ACCESS_TOKEN_EXPIRE__MINUTES)):
    date_expiration = datetime.now(timezone.utc) + token_duration
    dic_information = {'sub': id_user, 'exp': date_expiration }
    encoded_jwt = jwt.encode(dic_information, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def authenticate_user(email, password, session):
    user = session.query(User).filter(User.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user


@auth_router.get('/')
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"message": 'Vc acessou a rota auth', "authenticate":False}

@auth_router.post('/create_user')
async def create_user(user_schemas: UserSchema, session = Depends(get_session)):
    user =  session.query(User).filter(User.email==user_schemas.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Email do usuario já cadastrado')
    else:
        encrypted_password = bcrypt_context.hash(user_schemas.password)
        new_user = User(user_schemas.name, user_schemas.email, encrypted_password, user_schemas.active, user_schemas.admin)
        session.add(new_user)
        session.commit()
        return {'message': f'Usuario criado com sucesso {user_schemas.email}'}


@auth_router.post('/login')
async def login(login_schema: LoginSchema, session = Depends(get_session)):
    user = authenticate_user(login_schema.email, login_schema.password, session)
    if not user:
        raise HTTPException(status_code=400, detail='Usuario não encontrado ou credenciais inválidas')
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, token_duration=timedelta(days=7))
        return {'access_token': access_token, 'refresh_token': refresh_token , 'token_type': 'Bearer'}

@auth_router.get('/refresh')
async def use_refresh_token(user:User = Depends(verify_token)):
    access_token = create_token(user.id)
    return {'access_token': access_token, 'token_type': 'Bearer'}

