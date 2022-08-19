from typing import List

from sqlalchemy import (
    create_engine, literal_column, insert, update, delete
)
from sqlalchemy.orm import Session

from src.domain.sales_statistics.output.sales_statistics_repository import SalesStatisticsRepository
from src.domain.sales_statistics.sales_statistics import SalesStatistics
from src.infrastructure.entities.mapper.sales_statistics_mapper import SalesStatisticsMapper
from src.infrastructure.entities.models import SalesStatisticsEntity


class SalesStatisticsRepositoryImpl(SalesStatisticsRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def get(self, supplier_id: int, month: int) -> SalesStatistics: #necesita el año?
        with Session(bind=self.__connection) as session:
            result = session.query(SalesStatisticsEntity) \
                .filter(SalesStatisticsEntity.supplier_id == supplier_id).one()
            if not result:
                raise Exception('Record not found')
            return SalesStatisticsMapper.entity_to_domain(result)

