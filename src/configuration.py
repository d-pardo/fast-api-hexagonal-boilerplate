import os

import inject

from src.domain.category.category_service_impl import CategoryServiceImpl
from src.domain.category.input.category_service import CategoryService
from src.domain.category.output.category_repository import CategoryRepository
from src.domain.product.input.product_service import ProductService
from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product_service_impl import ProductServiceImpl
from src.domain.sales_statistics.input.sales_statistics_service import SalesStatisticsService
from src.domain.sales_statistics.output.sales_statistics_repository import SalesStatisticsRepository
from src.domain.sales_statistics.sales_statistics_service_impl import SalesStatisticsServiceImpl
from src.infrastructure.adapters.output.repositories.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.adapters.output.repositories.product_repository_impl import ProductRepositoryImpl
from src.infrastructure.adapters.output.repositories.sales_statistics_repository_impl import SalesStatisticsRepositoryImpl


def configure_inject() -> None:
    def config(binder: inject.Binder) -> None:
        database_uri = "postgresql://{}:{}@{}:{}/{}".format(
            os.getenv("DATABASE_USER"),
            os.getenv("DATABASE_PASSWORD"),
            os.getenv("DATABASE_HOST"),
            os.getenv("DATABASE_PORT"),
            os.getenv("DATABASE_APPLICATION"),
        )
        binder.bind(ProductRepository, ProductRepositoryImpl(database_uri))
        binder.bind(ProductService, ProductServiceImpl(ProductRepositoryImpl(database_uri)))
        
        binder.bind(CategoryRepository, CategoryRepositoryImpl(database_uri))
        binder.bind(CategoryService, CategoryServiceImpl(CategoryRepositoryImpl(database_uri)))
        
        binder.bind(SalesStatisticsRepository, SalesStatisticsRepositoryImpl(database_uri))
        binder.bind(SalesStatisticsService, SalesStatisticsServiceImpl(SalesStatisticsRepositoryImpl(database_uri)))

    inject.configure(config)
