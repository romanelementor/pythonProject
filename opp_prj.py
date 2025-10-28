# project Online store
from abc import ABC, abstractmethod
import datetime

class Product:
    def __init__(self, name, price, quantity, category):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def get_price(self):
        return self._price

    @property
    def get_category(self):
        return self._category

    @property
    def get_quantity(self):
        return self._quantity

    @price.setter
    def price(self, value):
        self._price = value

    @category.setter
    def category(self, value):
        self._category = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

class Order:
    def __init__(self, order_id, products, customer, order_date):
        self._order_id = order_id
        self._products = products
        self._customer = customer
        self._order_date = order_date

    def get_order_id(self):
        return self._order_id

    def get_products(self):
        return self._products

    def get_customer(self):
        return self._customer

    def get_order_date(self):
        return self._order_date

    def add_product(self, product):
        self._products.append(product)

class Customer:
    def __init__(self, name, email, address):
        self._name = name
        self._email = email
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, value):
        self._name = value

    @address.setter
    def address(self, value):
        self._address = value

