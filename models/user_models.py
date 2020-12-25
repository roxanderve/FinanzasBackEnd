from pydantic import BaseModel
from datetime import datetime

# Modelo de usuario de ingreso al sistema
class UserIn(BaseModel):
    username: str
    password: str

# Modelo de usuario para mostrar al público
class UserOut(BaseModel):
    nombres: str
    apellidos: str
    fecha_registro: datetime
    email: str