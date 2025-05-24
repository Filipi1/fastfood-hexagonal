import importlib
import inspect
import os
from http import HTTPMethod
from typing import Any, Optional, Sequence, List, Union, Type
from enum import Enum

from fastapi import APIRouter, FastAPI
from .interfaces import ControllerOptions
from .ports import APIController


class FastAPIManager:
    @staticmethod
    def normalize_api_path(path: str) -> str:
        if not path.startswith("/"):
            path = f"/{path}"
        if "_" in path:
            path = path.replace("_", "-")
        return path.lower()

    @staticmethod
    def __get_controllers() -> list[APIController]:
        instances: List[APIController] = []

        for root, _, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith("_controller.py"):
                    module_path = FastAPIManager.__get_module_path(root, file)
                    controller = FastAPIManager.__get_controller_from_module(
                        module_path
                    )
                    if controller:
                        instances.append(controller)

        return instances

    @staticmethod
    def __get_module_path(root: str, file: str) -> str:
        file_path = os.path.join(root, file)
        module_path = os.path.relpath(file_path, os.getcwd())
        module_path = module_path.replace(os.sep, ".").replace(".py", "")
        if module_path.startswith("src."):
            module_path = module_path[4:]
        return module_path

    @staticmethod
    def __get_controller_from_module(module_path: str) -> APIController | None:
        try:
            module = importlib.import_module(module_path)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if FastAPIManager.__is_valid_controller(name, obj):
                    return obj()
        except ImportError as e:
            print(f"Erro ao importar módulo {module_path}: {e}")
        return None

    @staticmethod
    def __is_valid_controller(name: str, obj: Type) -> bool:
        return (
            name != APIController.__name__
            and name.endswith("Controller")
            and issubclass(obj, APIController)
        )

    @staticmethod
    def initialize(api: FastAPI, prefix: str = ""):
        for controller in FastAPIManager.__get_controllers():
            api.include_router(controller.router, prefix=prefix)

    @staticmethod
    def controller(prefix: str, options: ControllerOptions):
        """Para o correto funcionamento do decorador, a classe deve herdar APIController, seu arquivo deve ser nomeado como *_controller.py e a classe deve ser nomeada como *Controller"""

        def decorator(cls):
            class Wrapper(cls, APIController):
                def __init__(self, *args, **kwargs):
                    tags: List[Union[str, Enum]] | None = (
                        [options.tags]
                        if isinstance(options.tags, str)
                        else options.tags
                    )
                    version = options.version
                    self.router = APIRouter(prefix=f"/{version}/{prefix}", tags=tags)
                    super().__init__(*args, **kwargs)
                    self.__register_routes()

                def __register_routes(self):
                    for attr_name in dir(self):
                        attr = getattr(self, attr_name)
                        if hasattr(attr, "_route"):
                            (
                                path,
                                method,
                                dependencies,
                                summary,
                                description,
                                response_model,
                            ) = attr._route
                            self.router.add_api_route(
                                path,
                                attr,
                                methods=[method],
                                dependencies=dependencies,
                                summary=summary,
                                description=description,
                                response_model=response_model,
                            )

            return Wrapper

        return decorator

    @staticmethod
    def route(
        path: str,
        method: HTTPMethod,
        dependencies: Optional[Sequence] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_model: Optional[Any] = None,
    ):
        normalized_path = FastAPIManager.normalize_api_path(path)

        def decorator(func):
            func._route = (
                normalized_path,
                method.value,
                dependencies,
                summary,
                description,
                response_model,
            )
            return func

        return decorator
