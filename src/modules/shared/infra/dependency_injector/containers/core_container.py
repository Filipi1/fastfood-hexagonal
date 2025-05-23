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
from modules.categories.application.use_cases.get_category_by_id_use_case import (
    GetCategoryByIdUseCase,
)
from modules.categories.domain.repositories.categories_repository import (
    CategoryRepository,
)
from modules.categories.domain.services.get_category_by_id_service import (
    GetCategoryByIdService,
)
from modules.order.application.use_cases.complete_order import CompleteOrderUseCase
from modules.order.application.use_cases.create_new_order import CreateNewOrderUseCase
from modules.order.domain.repositories.order_repository import OrderRepository
from modules.order.domain.services.complete_order import CompleteOrderService
from modules.order.domain.services.create_order import CreateOrderService
from modules.products.application.use_cases.create_product import CreateProductUseCase
from modules.products.application.use_cases.get_product import GetProductUseCase
from modules.products.application.use_cases.get_product_by_category import (
    GetProductByCategoryUseCase,
)
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.products.domain.services.add_product_service import AddProductService
from modules.products.domain.services.get_all_products_by_codes import (
    GetAllProductsByCodesService,
)
from modules.products.domain.services.get_product_by_category_service import (
    GetProductByCategoryService,
)
from modules.products.domain.services.get_product_service import GetProductService
from modules.user.application.use_cases.create_user_use_case import CreateUserUseCase
from modules.user.domain.repositories.user_repository import UserRepository
from modules.user.domain.services.create_user_service import CreateUserService
from modules.user.domain.services.get_user_by_email_and_password import (
    GetUserByEmailService,
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
    product_repository = providers.Singleton(
        ProductRepository,
        database=mongo_database,
    )
    category_repository = providers.Singleton(
        CategoryRepository,
        database=mongo_database,
    )
    order_repository = providers.Singleton(
        OrderRepository,
        database=mongo_database,
    )

    # INFRA SERVICES
    jwt_service = providers.Singleton(
        JWTService,
        secret_key=config.AUTH_SECRET_KEY,
        algorithm=config.AUTH_ALGORITHM,
        secret_key_no_auth=config.NO_AUTH_SECRET_KEY,
        algorithm_no_auth=config.NO_AUTH_ALGORITHM,
    )

    # USER =====================================================================

    # USER - SERVICES
    get_user_by_email_service = providers.Factory(
        GetUserByEmailService,
        user_repository=user_repository,
    )
    create_user_service = providers.Factory(
        CreateUserService,
        user_repository=user_repository,
    )

    # USER - USE CASES
    create_user_use_case = providers.Factory(
        CreateUserUseCase,
        create_user_service=create_user_service,
    )


    # AUTHENTICATION ===========================================================

    # AUTHENTICATION - SERVICES
    do_authentication_anonymous_service = providers.Singleton(
        DoAnonymousAuthenticationService, jwt_service=jwt_service
    )
    do_authentication_service = providers.Singleton(
        DoAuthenticationService,
        jwt_service=jwt_service,
        get_user_by_email_service=get_user_by_email_service,
    )

    # AUTHENTICATION - USE CASES
    authenticate_use_case = providers.Singleton(
        AuthenticateUseCase,
        do_anonymous_authentication_service=do_authentication_anonymous_service,
        do_authentication_service=do_authentication_service,
    )

    # CATEGORIES =================================================================

    # CATEGORIES SERVICES
    get_category_by_id_service = providers.Singleton(
        GetCategoryByIdService,
        category_repository=category_repository,
    )

    # CATEGORIES - USE CASES
    get_category_by_id_use_case = providers.Singleton(
        GetCategoryByIdUseCase,
        get_category_by_id_service=get_category_by_id_service,
    )

    # PRODUCTS =================================================================

    # PRODUCTS SERVICES
    add_product_service = providers.Singleton(
        AddProductService,
        product_repository=product_repository,
    )

    get_product_service = providers.Singleton(
        GetProductService,
        product_repository=product_repository,
    )
    get_product_by_category_service = providers.Singleton(
        GetProductByCategoryService,
        product_repository=product_repository,
    )
    get_all_products_by_codes_service = providers.Singleton(
        GetAllProductsByCodesService,
        product_repository=product_repository,
    )

    # PRODUCTS - USE CASES
    get_product_use_case = providers.Singleton(
        GetProductUseCase,
        get_product_service=get_product_service,
    )
    get_product_by_category_use_case = providers.Singleton(
        GetProductByCategoryUseCase,
        get_product_by_category_service=get_product_by_category_service,
    )
    create_product_use_case = providers.Singleton(
        CreateProductUseCase,
        add_product_service=add_product_service,
        get_category_by_id_use_case=get_category_by_id_use_case,
    )

    # ORDER ====================================================================

    # ORDER SERVICES
    create_order_service = providers.Singleton(
        CreateOrderService,
        order_repository=order_repository,
        get_all_products_by_codes_service=get_all_products_by_codes_service,
    )
    complete_order_service = providers.Singleton(
        CompleteOrderService,
        order_repository=order_repository,
    )

    # ORDER - USE CASES
    create_new_order_use_case = providers.Singleton(
        CreateNewOrderUseCase,
        create_order_service=create_order_service,
    )
    complete_order_use_case = providers.Singleton(
        CompleteOrderUseCase,
        complete_order_service=complete_order_service,
    )
