from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from gomongo import GoDatabase

from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.authentication.application.use_cases.authenticate import (
    AuthenticateUseCase,
)
from modules.authentication.domain.services.do_anonymous_authentication import (
    DoAnonymousAuthenticationService,
)
from modules.authentication.domain.services.do_authentication import (
    DoAuthenticationService,
)
from modules.products.application.use_cases.create_product import CreateProductUseCase
from modules.products.application.use_cases.get_product import GetProductUseCase
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.products.domain.services.add_product_service import AddProductService
from modules.products.domain.services.get_product_service import GetProductService
from modules.user.domain.repositories.user_repository import UserRepository
from modules.user.domain.services.get_user_by_email_and_password import (
    GetUserByEmailAndPasswordService,
)


class CoreContainer(DeclarativeContainer):
    config = providers.Configuration()

    config.MONGO_CONNECTION_STRING.from_env("MONGO_CONNECTION_STRING", as_=str)
    config.MONGO_DATABASE_NAME.from_env("MONGO_DATABASE_NAME", as_=str)
    config.AUTH_SECRET_KEY.from_env("AUTH_SECRET_KEY", as_=str)
    config.AUTH_ALGORITHM.from_env("AUTH_ALGORITHM", as_=str)
    config.NO_AUTH_SECRET_KEY.from_env("NO_AUTH_SECRET_KEY", as_=str)
    config.NO_AUTH_ALGORITHM.from_env("NO_AUTH_ALGORITHM", as_=str)

    mongo_database = providers.Singleton(
        GoDatabase,
        connection_string=config.MONGO_CONNECTION_STRING,
        database_name=config.MONGO_DATABASE_NAME,
    )

    # REPOSITORIES
    user_repository = providers.Singleton(
        UserRepository,
        database=mongo_database,
    )

    # DOMAIN SERVICES
    get_user_by_email_and_password_service = providers.Factory(
        GetUserByEmailAndPasswordService,
        user_repository=user_repository,
    )

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
        DoAuthenticationService,
        jwt_service=jwt_service,
        get_user_by_email_and_password_service=get_user_by_email_and_password_service,
    )

    # USE CASES
    authenticate_use_case = providers.Singleton(
        AuthenticateUseCase,
        do_anonymous_authentication_service=do_authentication_anonymous_service,
        do_authentication_service=do_authentication_service,
    )

    product_repository = providers.Singleton(
        ProductRepository,
        database=mongo_database,
    )
    add_product_service = providers.Singleton(
        AddProductService,
        product_repository=product_repository,
    )
    create_product_use_case = providers.Singleton(
        CreateProductUseCase,
        add_product_service=add_product_service,
    )
    get_product_service = providers.Singleton(
        GetProductService,
        product_repository=product_repository,
    )
    get_product_use_case = providers.Singleton(
        GetProductUseCase,
        get_product_service=get_product_service,
    )
