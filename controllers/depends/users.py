from typing import Optional

from config import database
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import BaseModel, ValidationError

from models.users import User
from security import SECRET_KEY, JWT_ALGORITHM


class TokenPayload(BaseModel):
    sub: Optional[int] = None


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/usuarios/login"
)


async def get_usuario_logado(
    token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    sql = f"""
        SELECT * FROM users WHERE id = {token_data.sub}
    """
    user = await database.fetch_one(sql)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return payload
