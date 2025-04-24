from dotenv import load_dotenv
from fastapi import FastAPI

from modules.infra.dependency_injector.containers import CoreContainer
from modules.shared.adapters.presentation.decorators import FastAPIManager

load_dotenv(override=True)

container = CoreContainer()
container.wire(modules=[__name__])
app = FastAPI(
    title="API",
    description="API para o sistema de fastfood",
    version="0.1.0",
    docs_url="/docs",
    prefix="/api",
)

FastAPIManager.initialize(app)
