from sqlalchemy import (
    Column, Integer, Text, Numeric, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CategoryEntity(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    products = relationship("ProductEntity", back_populates="category", lazy=True)


class ProductEntity(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    stock = Column(Numeric, nullable=False)
    price = Column(Numeric, nullable=False)
    pvp = Column(Numeric, nullable=False)
    has_discount = Column(Boolean, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("CategoryEntity", back_populates="products", lazy=True)


class SalesStatisticsEntity(Base):
    __tablename__ = 'sales_statistics'
    id = Column(Integer, primary_key=True)
    amount = Column(Numeric, nullable=False)
    average_amount = Column(Numeric, nullable=False)
    total_orders = Column(Numeric, nullable=False)
    supplier_id = Column(Integer, nullable=False)
