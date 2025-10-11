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

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

for key,value in grades.items():
    print(f"Name: {key}, Grade: {value}")

product_apple = {"name":"apple", "size":"small", "price":100}
#print(product_apple.keys())
#print(product_apple.values())
#print(product_apple["name"])

#inner dict
products = {"apple": {"name":"apple", "size":"small", "price":100},
            "bannana": {"name":"bannana", "size":"medium", "price":200},
            "orange": {"name":"orange", "size":"large", "price":300}
    }

#t5 key in dictionary
products = {"apple": 2, "banana": 1, "milk": 3}
p_name = input("enter product")
p_price = input("enter price")
if p_name in products:
    print(f"product {p_name} is already in the dict and price is : {products[p_name]}")
else:
    print("product is not in the dict")

#t6 word count
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_dict = {}
for word in words:
    words_dict[word] = words_dict.get(word,0)  + 1

print(words_dict)

#t7
salaries = {"John": 5000, "Emma": 5500, "Kelly": 6000, "Mike": 4500}
