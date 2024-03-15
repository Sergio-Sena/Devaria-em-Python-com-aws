from fastapi import APIRouter, Body, HTTPException
from services.AuthService import gerar_token_jwt
from models.usuarioModel import usuarioLoginModel
from services.AuthService import login_service

router = APIRouter()


@router.post('/login')
async def login(usuario: usuarioLoginModel = Body(...)):
    resultado = await login_service(usuario)

    # Aguarde a execução da coroutine
    if 'status' in resultado and resultado['status'] == 200:
        # Faça algo com o resultado
        del resultado["dados"]["senha"]

        token = gerar_token_jwt(resultado["dados"]["id"])

        resultado["dados"]['token'] = token

        return resultado
    else:
        raise HTTPException(status_code=resultado.get(
            'status', 500), detail=resultado.get('mensagem', 'Erro desconhecido'))
