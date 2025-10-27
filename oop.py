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


# Composition – Library & Books
class Book:
    def __init__(self,title, auther):
        self.title = title
        self.auther = auther

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"The book {book.title}, by {book.auther}")

b1 = Book("1984", "George Orwell")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.show_books()


# Challenge 4: Inheritance Chain – Employee Hierarchy#Challenge 4: Inheritance Chain – Employee Hierarchy
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
        print("this is Person class constructor")

    def display(self):
        print(f"name: {self.name}, age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print("this is Employe class constructor")

    def display(self):
        super().display()
        print(f"salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, salary, dept):
        super().__init__(name, age, salary)
        self.dept = dept
        print("this is Manager class constructor")

    def display_info(self):
        super().display()
        print(f"dept:{self.dept}")

m1 = Manager("John", 35, 80000, "IT")
m1.display_info()


# Challenge 5 - Polymorphism + Composition – Shape Area Calculator
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        "this is abs method area"
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
class ShapeCalculator:
    def __init__(self, shapesList):
        self.shapesList = shapesList

    def total_area(self):
        total = 0
        for shape in self.shapesList:
            print(shape.area())
            total = total + shape.area()
        return total


s1 = Circle(5)
s2 = Rectangle(5,10)
shapes = [s1, s2]
sc = ShapeCalculator(shapes)
sc.total_area()


# Challenge 6: Design Pattern – Singleton Logger
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)

    def show_logs(self):
        return self.logs

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True
logger1.log("System started.")
print(logger2.show_logs())
logger2.log("User logged in.")
print(logger2.show_logs())
