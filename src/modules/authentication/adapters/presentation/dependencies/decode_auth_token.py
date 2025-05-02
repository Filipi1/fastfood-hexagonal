from fastapi import HTTPException, Request

from modules.authentication.adapters.dtos import AuthTokenData
from modules.shared.infra.dependency_injector.containers import AuthenticationContainer


async def decode_auth_token(request: Request) -> AuthTokenData:
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail={"message": "Token inválido"})
    token = token.split(" ")[1] if len(token.split(" ")) > 1 else token
    decoded_token = AuthenticationContainer.jwt_service().decode_token(token)
    if not decoded_token:
        raise HTTPException(status_code=401, detail={"message": "Token inválido"})
    return AuthTokenData(**decoded_token)
