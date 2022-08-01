# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("3")
start = datetime.datetime.strptime("25-06-2022", "%d-%m-%Y")
end = datetime.datetime.strptime("01-07-2022", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
print(date_generated)

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))

for index, day_to_check in enumerate(date_generated):
    date_to_check = str(day_to_check.date())
    print(str(index) + ' ' + date_to_check)


# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

print('4')
start_date = datetime.datetime.strptime('2022-04-23', '%Y-%m-%d')
end_date = datetime.datetime.today().date()
print(start_date, end_date)

date_to_check = str(start_date.date())
print(date_to_check)

fruit = 'Apple2'
isApple = True if fruit == 'Apple' else False
print(isApple)