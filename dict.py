from itertools import islice

my_dict = {"Israel": "Jerusalem", "USA": "Vashngton D.C.", "Italy": "Rome"}
print(my_dict)
first_key = list(my_dict.keys())[0]
first_val = list(my_dict.values())[0]
print(f"{first_key} is {first_val}")

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
grades["Dav"] = 100
grades["Dav"] = 101
print(grades)

print(grades.keys())
print(grades.values())
print(grades.items())

item1 = grades["Bob"]
print(item1)
second_item = next(islice(grades.values(), 2, None))
print(second_item)