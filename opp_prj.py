# project Online store
from abc import ABC, abstractmethod
import datetime

class Product:
    def __init__(self, name, price, stock, category):
        self._name = name
        self._price = price
        self._stock = stock
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
    def get_stock(self):
        return self._stock

    @price.setter
    def price(self, value):
        self._price = value

    @category.setter
    def category(self, value):
        self._category = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def __str__(self) -> str:
        return f"Product data: {self._name}, price: {self._price}, stock: {self._stock}, category: {self._category}"


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

    def __str__(self) -> str:
        return f"Customer data: {self._name}, {self._email}, {self._address}"


class CartItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    def get_product(self):
        return self._product

    def get_quantity(self):
        return self._quantity

    def get_total(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"CartItem data: {self._product}, {self._quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, cart_item):
        self.items.append(cart_item)

    def remove_item(self, cart_item):
        self.items.remove(cart_item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_total()
        return total

    def __str__(self) -> str:
        return f"ShoppingCart data: {self.items} total: {self.get_total()}"

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

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
