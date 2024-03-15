from fastapi import APIRouter, Body, Depends, HTTPException, Header
from middleware.JWT_middleware import verificar_token
from models.usuarioModel import usuarioCriarModel
from services.AuthService import decodificar_token_jwt
from services.UsuarioService import registrar_usuario, buscar_usuario_logado

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo usuário.")
async def rota_criar_usuario(usuario: usuarioCriarModel = Body(...)):
    try:
        resultado = await registrar_usuario(usuario)
        if not resultado['status'] == 201:
            raise HTTPException(status_code=500, detail="Erro interno no servidor")
        return resultado
    except Exception as erro:
        print(erro)

@router.get(
    '/me',
    response_description='Rota para buscar informações de usuário logado.',
    dependencies=[Depends(verificar_token)]
)
async def buscar_info_usuario_logado(Authorization: str = Header(default="")):
    try:
        token = Authorization.split()[1]  # Correção aqui

        payload = decodificar_token_jwt(token)
        
        usuario = buscar_usuario(payload["usuario_id"])
        return buscar_usuario_logado

    except:
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
