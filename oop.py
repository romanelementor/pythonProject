# t1
class Car:
    # Class attributes
    brand = ''
    model = ''
    year = 1900

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car details : {self.brand}, {self.model}, {self.year}")
              
car_1 = Car("Toyota", "Corola", 2019)
car_2 = Car("Mazda", "323", 1994)

car_1.display_info()
car_2.display_info()


# t2 Encapsulation
class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance = self._balance + amount

    def withdraw(self, amount):
        self._balance = self._balance - amount

    def get_balance(self):
        return self._balance
      
b1 = BankAccount()
b1.deposit(101)
b1.withdraw(200)
b1.get_balance()


# t3 Multiple Inheritance
class Flyable:
    def fly(self):
        print("Flying high!")

class Swimmable:
    def swim(self):  
        print("Swimming fast!")

class Duck(Flyable, Swimmable):
    def make_sound(self):
        print("Quack!")

a = Flyable()
b = Swimmable()
c = Duck()

c.fly()
c.swim()
c.make_sound()


# t4 Polymorphism
class Cat:
    def sound(self):
        return "meuooo !"

class Dog:
    def sound(self):
        return "hoo hoo !"

class Cow:
    def sound(self):
        return "moo !"

list_obj = []

list_obj.append(Cat())
list_obj.append(Dog())
list_obj.append(Cow())

for obj in list_obj:
    print(obj.sound())


# t5 class method and static method
class Employee:
    company_name = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
    
    @classmethod
    def print_company(cls):
        print(cls.company_name)

    @staticmethod
    def add(a, b):
        return a +b
    
    @staticmethod
    def print_static(s):
        print(f"This is a static method : {s}")
    
    def __str__ (self):
        return f"instance print method: {self.name} {self.salary}"
    
company1 = Employee("John", 10000)
company2 = Employee("Ron", 20000)
print(company1)
print(company2)

Employee.change_company("DBT")
Employee.print_company()
company2.change_company("DBT v2")
Employee.print_company()

print(Employee.add(10,20))
Employee.print_static("hi")

# t6 Dunder/magic Methods (__str__, __add__)
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Point objects: {type(other)}")

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # (6, 8)


# Challenge 1: Abstract Class – Payment System
from abc import ABC, abstractmethod

class Payment(ABC): 
    @abstractmethod
    def pay(amount):
        """This is abstract method must be implemented by all subclasses"""
        pass
class CreditCardPayment(Payment):
    def __init__(self,amount):
        self.amount = amount

    def pay(self, amount):
        return f"Paid {amount} using Credit Card"
    
    def __str__(self):
        return self.pay(self.amount)
        
        
class PayPalPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def pay(self, amount):
        return f"Paid {amount} using PayPal"
    
    def __str__(self):
        return self.pay(self.amount)
    
pay1 = CreditCardPayment(100)
pay2 = PayPalPayment(1000)

print(f" First print {pay1}")
print(f" First print {pay2}")

l = [pay1, pay2]
for obj in l:
    print(obj)


# Challenge 2: Property Decorators – Temperature Converter
# Challenge 2: Property Decorators – Temperature Converter
c# Challenge 2: Property Decorators – Temperature Converter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        print("this is a getter !")
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        print("This is a setter !")
        if value < -273.15:
            raise ValueError("Not good value")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
        
t1 = Temperature(25)
print(t1.fahrenheit)
t1.fahrenheit = 32
print(t1.fahrenheit)