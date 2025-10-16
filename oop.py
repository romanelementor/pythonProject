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


# t2 BankAccount
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


# t3
