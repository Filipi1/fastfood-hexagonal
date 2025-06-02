from fastapi import Request
from fastapi.responses import JSONResponse
from .application_exception import ApplicationException


async def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=400, content={"status": 400, "message": exc.message}
    )


async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": 500,
            "message": "Ocorreu um problema, por favor, tente novamente.",
        },
    )
