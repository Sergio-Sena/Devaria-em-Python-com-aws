from pydantic import BaseModel, Field, EmailStr

class usuarioModel(BaseModel):
    id: str = Field(...)
    nome: str= Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario":{
                "nome":"Falano",
               "email":"Fulano@gmail.com",
            "senha":"Senha1234!",
        "foto": "fulano.png"
            }
        }

class usuarioCriarModel(BaseModel):
    nome: str= Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario":{
                "nome":"Falano",
               "email":"Fulano@gmail.com",
            "senha":"Senha1234!",
        "foto": "fulano.png"
            }
        }

class usuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario":{
               "email":"Fulano@gmail.com",
            "senha":"Senha1234!",
                "status":200

            }
        }