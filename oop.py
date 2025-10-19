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


# t5 