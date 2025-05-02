from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.authentication.application.use_cases.authenticate import (
    AuthenticateUseCase,
)
from modules.authentication.domain.services import (
    DoAnonymousAuthenticationService,
    DoAuthenticationService,
)


class AuthenticationContainer(DeclarativeContainer):
    config = providers.Configuration()

    config.AUTH_SECRET_KEY.from_env("AUTH_SECRET_KEY", as_=str)
    config.AUTH_ALGORITHM.from_env("AUTH_ALGORITHM", as_=str)
    config.NO_AUTH_SECRET_KEY.from_env("NO_AUTH_SECRET_KEY", as_=str)
    config.NO_AUTH_ALGORITHM.from_env("NO_AUTH_ALGORITHM", as_=str)

    # INFRA SERVICES
    jwt_service = providers.Singleton(
        JWTService,
        secret_key=config.AUTH_SECRET_KEY,
        algorithm=config.AUTH_ALGORITHM,
        secret_key_no_auth=config.NO_AUTH_SECRET_KEY,
        algorithm_no_auth=config.NO_AUTH_ALGORITHM,
    )

    # DOMAIN SERVICES
    do_authentication_anonymous_service = providers.Singleton(
        DoAnonymousAuthenticationService, jwt_service=jwt_service
    )
    do_authentication_service = providers.Singleton(
        DoAuthenticationService, jwt_service=jwt_service
    )

    # USE CASES
    authenticate_use_case = providers.Singleton(
        AuthenticateUseCase,
        do_anonymous_authentication_service=do_authentication_anonymous_service,
        do_authentication_service=do_authentication_service,
    )
