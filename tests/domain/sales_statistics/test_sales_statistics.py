from typing import List
from unittest.mock import Mock

import inject
import pytest

from src.domain.sales_statistics.sales_statistics import (
    SalesStatistics
)
from src.domain.sales_statistics.sales_statistics_service_impl import SalesStatisticsServiceImpl
from src.domain.sales_statistics.output.sales_statistics_repository import SalesStatisticsRepository


@pytest.fixture
def sales_statistics_repository() -> Mock:
    return Mock()


@pytest.fixture
def injector(sales_statistics_repository: Mock) -> None:
    inject.clear_and_configure(lambda binder: binder
                               .bind(SalesStatisticsRepository, sales_statistics_repository))


@pytest.fixture
def sales_statistics() -> SalesStatistics:
    return SalesStatistics(id=1, amount = 20000, average_amount = 111.11, total_orders = 890)
# amount = Facturación, 
# Ticket Promedio = average_amount
# Total de pedido = total_orders


class TestSalesStatisticsServiceImpl:

    def test_should_return_sales_statistics_by_id(
            self, injector: None, sales_statistics_repository: Mock, sales_statistics: SalesStatistics):
        
        sales_statistics_repository.get.return_value = sales_statistics
        supplier_id=1
        month=2
        
        sales_statistics_result = SalesStatisticsServiceImpl().get(supplier_id, month)
        
        assert sales_statistics_result == sales_statistics
        assert isinstance(sales_statistics_result, SalesStatistics)
        sales_statistics_repository.get.assert_called_once_with(supplier_id, month)
