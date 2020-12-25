from db.user_db import UserInDB
from db.user_db import create_user, get_user, delete_user
from models.user_models import UserOut, UserIn
import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost", 
"http://localhost:8080",
"http://127.0.0.1", 
"http://127.0.0.1:8080",
]
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

#Consultar usuario
@api.get("/user/{username}")
async def get_user_information(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail="El usuario no existe.")
    if not user_in_db.active:
        raise HTTPException(status_code = 404, detail="El usuario ya no se encuentra activo.")
    user_out = UserOut(**user_in_db.dict())
    return user_out

#Crear usuario
@api.put("/user/create/")
async def add_user(user: UserInDB):
    create_user(user)
    user_out = UserOut(**user.dict())
    return user_out

#Dar de baja un usuario
@api.put("/user/delete/")
async def unsubscribe_user(user: UserIn):
    if delete_user(user):
        return {"message": "El usuario ha sido dado de baja."}
    else:
        raise HTTPException(status_code = 404, detail="El usuario no existe o la contraseña es incorrecta")

#Autenticación del usuario
@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail="El usuario no existe")
    if user_in_db.active == False:
        raise HTTPException(status_code = 404, detail="El usuario se encuentra inactivo")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code = 404, detail="La contraseña es incorrecta")
    else:
        return UserOut(**user_in_db.dict())