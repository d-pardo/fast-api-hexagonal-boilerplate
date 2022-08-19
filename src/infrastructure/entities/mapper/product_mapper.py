from src.domain.category.category import Category
from src.domain.product.product import Product, ProductCreateOut, ProductUpdateOut
from src.infrastructure.entities import ProductEntity


class ProductMapper:

    @staticmethod
    def entity_to_domain(product: ProductEntity):
        return Product(
            id=product.id,
            name=product.name,
            stock=product.stock,
            price=product.price,
            pvp=product.pvp,
            has_discount=product.has_discount,
            category=Category.from_orm(product.category)
        )


class ProductCreateOutMapper:
    @staticmethod
    def entity_to_domain(product: ProductEntity):
        return ProductCreateOut(
            id=product.id,
            name=product.name,
            stock=product.stock,
            price=product.price,
            pvp=product.pvp,
            has_discount=product.has_discount,
            category_id=product.category_id
        )


class ProductUpdateOutMapper:
    @staticmethod
    def entity_to_domain(product: ProductEntity):
        return ProductUpdateOut(
            id=product.id,
            name=product.name,
            stock=product.stock,
            price=product.price,
            pvp=product.pvp,
            has_discount=product.has_discount,
            category_id=product.category_id
        )
