from typing import List

import inject

from src.domain.product.input.product_service import ProductService
from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product import Product, ProductCreateOut, ProductUpdateOut, ProductCreateIn, ProductUpdateIn


class ProductServiceImpl(ProductService):

    @inject.autoparams()
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def list(self) -> List[Product]:
        return self.repository.list()

    def get(self, product_id: int) -> Product:
        return self.repository.get(product_id)

    def create(self, product: ProductCreateIn) -> ProductCreateOut:
        return self.repository.create(product)

    def update(self, product_id: int, product: ProductUpdateIn) -> ProductUpdateOut:
        return self.repository.update(product_id, product)

    def delete(self, product_id: int) -> None:
        self.repository.delete(product_id)
