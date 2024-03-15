from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def gerar_senha_criptografada(senha):
    return pwd_context.hash(senha)


def verificar_senha(senha, senha_criptografada):
    return pwd_context.verify(senha, senha_criptografada)
