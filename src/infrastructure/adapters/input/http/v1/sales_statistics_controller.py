import inject
from fastapi import APIRouter
from starlette import status

from src.domain.sales_statistics.input.sales_statistics_service import SalesStatisticsService
from src.domain.sales_statistics.sales_statistics import SalesStatistics

@inject.autoparams()
def sales_statistics_router(
        sales_statistics_service: SalesStatisticsService
) -> APIRouter:
    router = APIRouter(tags=["sales-statistics"])

    @router.get('/sales-statistics/{supplier_id}', response_model=SalesStatistics, status_code=status.HTTP_200_OK)
    async def get_sales_statistics_by_supplier(supplier_id: int, month: int) -> SalesStatistics:
        result = sales_statistics_service.get(supplier_id, month)
        return result.to_dict()
    
    return router