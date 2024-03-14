from typing import Optional
from fastapi import  FastAPI
from pydantic import BaseModel
from routes.usuarioRoute import router as UsuarioRoute
from routes.autenticacaoRoute import router as AutenticacaoRoute

app = FastAPI()

app.include_router(UsuarioRoute, tags=["Usuario"], prefix="/api/usuario")
app.include_router(AutenticacaoRoute, tags=["Autenticação"], prefix="/api/auth")

@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status":"ok"
    }