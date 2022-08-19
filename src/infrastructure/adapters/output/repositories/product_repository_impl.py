from typing import List

from sqlalchemy import (
    create_engine, literal_column, insert, update, delete
)
from sqlalchemy.orm import Session

from src.domain.product.exceptions import ProductNotFound
from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product import Product, ProductCreateOut, ProductCreateIn, ProductUpdateIn, ProductUpdateOut
from src.infrastructure.entities.mapper.product_mapper import (
    ProductMapper, ProductCreateOutMapper, ProductUpdateOutMapper
)
from src.infrastructure.entities.models import ProductEntity


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> List[Product]:
        with Session(bind=self.__connection) as session:
            products = session.query(ProductEntity)
            return [ProductMapper.entity_to_domain(product) for product in products]

    def get(self, product_id: int) -> Product:
        with Session(bind=self.__connection) as session:
            product = session.query(ProductEntity) \
                .filter(ProductEntity.id == product_id).one()
            if not product:
                raise ProductNotFound('Product does not found')
            return ProductMapper.entity_to_domain(product)

    def create(self, product: ProductCreateIn) -> ProductCreateOut:
        with Session(bind=self.__connection) as session:
            query = (
                insert(ProductEntity)
                .values(**product.dict())
                .returning(literal_column('*'))
            )
            cursor = session.execute(query)
            session.commit()
            result = cursor.fetchone()
            return ProductCreateOutMapper.entity_to_domain(result)

    def update(self, product_id: int, product: ProductUpdateIn) -> ProductUpdateOut:
        with Session(bind=self.__connection) as session:
            query = (
                update(ProductEntity)
                .values(**product.dict())
                .where(ProductEntity.id == product_id)
                .returning(literal_column('*'))
            )
            cursor = session.execute(query)
            session.commit()
            result = cursor.fetchone()
            return ProductUpdateOutMapper.entity_to_domain(result)

    def delete(self, product_id: int):
        with Session(bind=self.__connection) as session:
            query = (
                delete(ProductEntity).where(ProductEntity.id == product_id)
            )
            session.execute(query)
            session.commit()
