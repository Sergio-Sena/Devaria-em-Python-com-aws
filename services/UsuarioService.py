from models.usuarioModel import usuarioCriarModel
from repositories.UsuarioRepositories import (
    criar_usuario,
    buscar_usuario_por_email,
    buscar_usuario_logado,
    listar_usuario,
    atualizar_usuario,
    deletar_usuario
)


async def registrar_usuario(usuario: usuarioCriarModel):
    try:
        usuario_encontrado = await buscar_usuario_por_email(usuario.email)
        if usuario_encontrado:
            return {
                "mensagem": f'E-mail {usuario.email} ja resgistrado no sistema.',
                "dados": "",
                "Status": 400
            }
        else:
            novo_usuario = await criar_usuario(usuario)
            return {
                "mensagem": 'Usuario cadastrado com sucesso!',
                "dados": novo_usuario,
                "Status": 201
            }
    except Exception as error:
        return {
            "mensagem": 'Erro interno do servidor',
            "dados": str(error),
            "Status": 500
        }


async def buscar_usuario_logado(id: str):
    try:
        usuario_encontrado = await buscar_usuario(id)
        if usuario_encontrado:
            return usuario_encontrado
        else:
            return {
                "mensagem": f"Usuario com o id{id} não foi encontrado.",
                "dados": "",
                "Status": 404
            }
    except Exception as error:
        return {
            "mensagem": 'Erro interno do servidor',
            "dados": str(error),
            "Status": 500
        }
