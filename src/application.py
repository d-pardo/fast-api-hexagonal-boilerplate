from fastapi import FastAPI

from src.configuration import configure_inject
from src.infrastructure.adapters.input.http.utils.error_handler import ErrorHandler
from src.infrastructure.adapters.input.http.v1 import product_controller, sales_statistics_controller
from src.infrastructure.adapters.input.http.v1 import category_controller


def create_application() -> FastAPI:
    application = FastAPI()
    configure_inject()
    application.add_middleware(ErrorHandler)
    application.include_router(router=product_controller.product_router(), prefix='/v1')
    application.include_router(router=category_controller.category_router(), prefix='/v1')
    application.include_router(router=sales_statistics_controller.sales_statistics_router(), prefix='/v1')
    return application


app = create_application()
