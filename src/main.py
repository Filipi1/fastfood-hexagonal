from dotenv import load_dotenv
from fastapi import FastAPI

from modules.shared.infra.dependency_injector.containers import CoreContainer
from modules.shared.decorators import FastAPIManager
from modules.shared.exceptions.handlers import (
    application_exception_handler,
    global_exception_handler,
)
from modules.shared.exceptions.application_exception import ApplicationException

load_dotenv(override=True)

container = CoreContainer()
container.wire(modules=[__name__])
app = FastAPI(
    title="FastFood API",
    description="API para o sistema de fastfood",
    version="0.1.0",
    docs_url="/docs",
    prefix="/api",
)

app.add_exception_handler(ApplicationException, application_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

FastAPIManager.initialize(app)
