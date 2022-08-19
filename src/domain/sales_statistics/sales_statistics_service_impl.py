from typing import List

import inject
from src.domain.sales_statistics.input.sales_statistics_service import SalesStatisticsService
from src.domain.sales_statistics.output.sales_statistics_repository import SalesStatisticsRepository
from src.domain.sales_statistics.sales_statistics import SalesStatistics


class SalesStatisticsServiceImpl(SalesStatisticsService):

    @inject.autoparams()
    def __init__(self, repository: SalesStatisticsRepository):
        self.repository = repository

    def get(self, supplier_id: int, month: int) -> SalesStatistics:
        return self.repository.get(supplier_id, month)

