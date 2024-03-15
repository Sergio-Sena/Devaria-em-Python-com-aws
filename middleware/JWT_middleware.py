
from fastapi import HTTPException, Header

from services.AuthService import decodificar_token_jwt

#Bearer {Token} 
async def verificar_token(Authorization: str = Header(default="")):
    if not Authorization.startswith("Bearer"):
        raise HTTPException(status_code=401,detail="Necessario token para autenticação.")
    else:
        token = Authorization.split(" ")[1]
        
        payload = decodificar_token_jwt(token)

        if not payload:
            raise HTTPException(status_code=401,detail="Token invalido ou expirado")
        return payload
