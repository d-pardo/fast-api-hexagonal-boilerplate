from abc import (
    ABCMeta,
    abstractmethod
)
from typing import List

from src.domain.sales_statistics.sales_statistics import SalesStatistics


class SalesStatisticsRepository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, supplier_id: int, month: int) -> SalesStatistics:
        pass
