from abc import ABC, abstractmethod
import datetime

class Product:
	def __init__(self,name, stock, price):
		self._name = name
		self._stock = stock
		self.price = price

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def stock(self):
		return self._stock

	@stock.setter
	def stock(self, value):
		if value > 0:
			self._stock += value
		else:
			raise ValueError("setter will not work , value < =0 ")

class Customer:
	def __init__(self, id, name, address):
		self._id = id
		self._name = name
		self._address = address

	@property
	def name(self):
		print("customer getter")
		return self._name

	@property
	def address(self):
		print("custom getter address")
		return self._address

	@name.setter
	def name(self, value):
		self._name = value


class ItemCart:
	def __init__(self, product, quantity):
		self.product = product
		self.quantity = quantity

	def get_total(self):
		return self.quantity * self.product.price


class ShoppingCart:
	def __init__(self):
		self.items = []

	def add_item(self, product, quantity):
		if product.stock >= quantity :
			self.items.append(ItemCart(product, quantity))
		else:
			print(f"not enough {product.name} in stock. ")

	def get_total(self):
		return sum(item.get_total() for item in self.items)

	def show_cart(self):
		for item in self.items:
			print( f"Item is {item.product.name}, price is {item.get_total()}" )


class Payment(ABC):
	@abstractmethod
	def pay(self, amount):
		pass

class CreditCardPayment(Payment):
	def __init__(self, card_number):
		self. card_number = card_number

	def pay(self, amount):
		print(f"Paid ${amount:.2f}, {amount} using credit card")

class PayPalPayment(Payment):
	def __init__(self, email):
		self.email = email

	def pay(self, amount):
		print(f"This is PayPal payment")

class Logger:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		self.msg_list = []

	def log(self, msg):
		now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.msg_list.append(msg)
		print(f" {now} {msg}")

	def show_logs(self):
		return self.msg_list


class Order:
	def __init__(self, customer, shopping_cart, payment_method):
		self.customer= customer
		self.shopping_cart = shopping_cart
		self.payment_method = payment_method
		self.logger = Logger()

	def complete_order(self):
		total = self.shopping_cart.get_total()
		if total == 0:
			print("Cart is empty")
			return
		self.payment_method.pay(total)
		self.logger.log("Order completed")

	def add_to_logger(self):
		self.logger.log("This is a logger for order completion. " + str(self.shopping_cart.get_total()))

	def get_logs(self):
		return self.logger.show_logs()


# usage
if __name__ == "__main__":
    # Products
    p1 = Product("Laptop", 1200, 5)
    p2 = Product("Headphones", 150, 10)
    p3 = Product("Mouse", 40, 20)
    
    # Customer
    c1 = Customer(123, "Alice", "alice@example.com")

    print("Cart before adding items:")

    # Shopping Cart
    cart = ShoppingCart()
    cart.add_item(p1, 1)
    cart.add_item(p2, 2)
    cart.add_item(p3, 3)

    print("Cart items after adding items")

    cart.show_cart()

    print("Cart after adding items:")

    # Payment Method
    payment = PayPalPayment("alice@paypal.com")

    # Order
    order = Order(c1, cart, payment)
    order.complete_order()
    order.add_to_logger()
    print(order.get_logs())