from typing import List

from sqlalchemy import (
    create_engine, literal_column, insert, update, delete
)
from sqlalchemy.orm import Session

from src.domain.category.category import (
    Category, CategoryCreateIn, CategoryCreateOut, CategoryUpdateIn, CategoryUpdateOut
)
from src.domain.category.exceptions import CategoryNotFound
from src.domain.category.output.category_repository import CategoryRepository
from src.infrastructure.entities.mapper.category_mapper import (
    CategoryMapper, CategoryCreateOutMapper, CategoryUpdateOutMapper
)
from src.infrastructure.entities.models import CategoryEntity


class CategoryRepositoryImpl(CategoryRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> List[Category]:
        with Session(bind=self.__connection) as session:
            categories = session.query(CategoryEntity)
            return [CategoryMapper.entity_to_domain(category) for category in categories]

    def get(self, category_id: int) -> Category:
        with Session(bind=self.__connection) as session:
            category = session.query(CategoryEntity) \
                .filter(CategoryEntity.id == category_id).one()
            if not category:
                raise CategoryNotFound('Category does not found')
            return CategoryMapper.entity_to_domain(category)

    def create(self, category: CategoryCreateIn) -> CategoryCreateOut:
        with Session(bind=self.__connection) as session:
            query = (
                insert(CategoryEntity)
                    .values(**category.dict())
                    .returning(literal_column('*'))
            )
            cursor = session.execute(query)
            session.commit()
            result = cursor.fetchone()
            return CategoryCreateOutMapper.entity_to_domain(result)

    def update(self, category_id: int, category: CategoryUpdateIn) -> CategoryUpdateOut:
        with Session(bind=self.__connection) as session:
            query = (
                update(CategoryEntity)
                    .values(**category.dict())
                    .where(CategoryEntity.id == category_id)
                    .returning(literal_column('*'))
            )
            cursor = session.execute(query)
            session.commit()
            result = cursor.fetchone()
            return CategoryUpdateOutMapper.entity_to_domain(result)

    def delete(self, category_id: int):
        with Session(bind=self.__connection) as session:
            query = (
                delete(CategoryEntity).where(CategoryEntity.id == category_id)
            )
            session.execute(query)
            session.commit()
