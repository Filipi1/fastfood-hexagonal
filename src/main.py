import logging

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI

from modules.infra.dependency_injector.containers import CoreContainer
from modules.shared.adapters.presentation.decorators import FastAPIManager

load_dotenv(override=True)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

container = CoreContainer()
container.wire(modules=[__name__])

app = FastAPI(
    title="API",
    description="API para o sistema de e-commerce",
    version="1.0.0",
    docs_url="/docs",
    prefix="/api",
)

FastAPIManager.initialize(app)

logger = logging.getLogger("fastapi")
logger.log(level=logging.INFO, msg="Teste!")
