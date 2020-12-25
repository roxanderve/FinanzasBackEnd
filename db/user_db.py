from typing import Dict
from pydantic import BaseModel
from datetime import date
from datetime import datetime

# Definición de clase UserInDB con sus atributos
class UserInDB(BaseModel):
    username:str
    nombres: str
    apellidos: str
    email: str
    password:str
    active:  bool
    fecha_registro: datetime
    
    
db_users = Dict[str, UserInDB]

# Base de datos ficticia
db_users = {
    "carlitosmota": UserInDB(**{"username":"carlitosmota",
                                "nombres":"Carlos",
                                "apellidos":"Perez Mota",
                                "email":"capeta01@gmail.com",
                                "password":"123456",
                                "active":False,
                                "fecha_registro":"2012-05-01 05:34:01"}),

    "nando_duca": UserInDB(**{"username":"nando_duca",
                              "nombres":"Fernando",
                              "apellidos":"Duarte Camacho",
                              "email":"feducho2@gmail.com",
                              "password":"234567",
                              "active":True,
                              "fecha_registro":"2012-04-30 10:14:23"}),

    "maricami": UserInDB(**{"username":"maricami",
                            "nombres":"Maria camila",
                            "apellidos":"Estrada Tobon",
                            "email":"mariestrada@hotmail.com",
                            "password":"987654",
                            "active":False,
                            "fecha_registro":"2011-10-01 05:34:01"}),

    "crimar": UserInDB(**{"username":"crimar",
                                "nombres":"Cristina",
                                "apellidos":"Martinez Ortiz",
                                "email":"crimar01@hotmail.com",
                                "password":"5566214",
                                "active":False,
                                "fecha_registro":"2009-08-22 05:41:12"}),

    "meligar": UserInDB(**{"username":"meligar",
                              "nombres":"Melissa",
                              "apellidos":"Garcia Gomez",
                              "email":"meligar80@gmail.com",
                              "password":"965621",
                              "active":True,
                              "fecha_registro":"2011-11-30 04:51:20"}),

    "nata": UserInDB(**{"username":"nata",
                            "nombres":"Natalia Andrea",
                            "apellidos":"Pino",
                            "email":"pinonata@hotmail.com",
                            "password":"124515",
                            "active":True,
                            "fecha_registro":"2014-08-20 09:14:41"}),                                                    
}

def get_user(username: str):
    """Retorna el usuario buscándolo por su username. En caso de no encontrarlo retorna None"""
    if username in db_users.keys():
        return db_users[username]
    else:
        return None

def delete_user(user: UserInDB):
    """Busca el usuario en la base de datos y compara su contraseña. En caso de encontrarlo y verificarlo
    cambia su estado de actividad a inactivo y retorna verdadero. Caso contrario retorna falso"""
    user_in_db = get_user(user.username)
    if user_in_db:
        if user.password == user_in_db.password:
            user_in_db.active = False
            return True
        else:
            return False
    else:
        return False

def create_user(new_user: UserInDB):
    """Crea un nuevo usuario con la información que le entra por parámetro"""
    if get_user(new_user.username) == None:
        db_users[new_user.username] = new_user