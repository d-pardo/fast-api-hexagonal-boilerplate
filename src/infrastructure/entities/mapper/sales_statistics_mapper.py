from src.domain.sales_statistics.sales_statistics import SalesStatistics
from src.infrastructure.entities.models import SalesStatisticsEntity


class SalesStatisticsMapper:

    @staticmethod
    def entity_to_domain(sales_statistics: SalesStatisticsEntity):
        return SalesStatistics(
            id=sales_statistics.id,
            amount= sales_statistics.amount,
            average_amount= sales_statistics.average_amount,
            total_orders= sales_statistics.total_orders
        )

