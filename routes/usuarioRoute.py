from fastapi import APIRouter, Body, HTTPException
from models.usuarioModel import usuarioCriarModel
from services.UsuarioService import (
    registrar_usuario
)

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo usuário.")
async def rota_criar_usuario(usuario: usuarioCriarModel = Body(...)):
    resultado = await registrar_usuario(usuario)

    return resultado
