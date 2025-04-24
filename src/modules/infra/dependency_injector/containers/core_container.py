from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from modules.infra.dependency_injector.containers import AuthenticationContainer


class CoreContainer(DeclarativeContainer):
    config = providers.Configuration()

    authentication_container = providers.Container(AuthenticationContainer)
