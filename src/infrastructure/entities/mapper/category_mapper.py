from src.domain.category.category import Category, CategoryCreateOut, CategoryUpdateOut
from src.infrastructure.entities import CategoryEntity


class CategoryMapper:

    @staticmethod
    def entity_to_domain(category: CategoryEntity):
        return Category(
            id=category.id,
            name=category.name
        )


class CategoryCreateOutMapper:
    @staticmethod
    def entity_to_domain(category: CategoryEntity):
        return CategoryCreateOut(
            id=category.id,
            name=category.name,
        )


class CategoryUpdateOutMapper:
    @staticmethod
    def entity_to_domain(category: CategoryEntity):
        return CategoryUpdateOut(
            id=category.id,
            name=category.name
        )
