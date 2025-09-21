# Square Numbers with map
l1 = [1, 2, 3, 4, 5, 6]

res_1 = map(lambda x:x*x, l1)
list_res_1 = list(res_1)

print(list_res_1)

# strings to uppercase with map
l2 = ["python", "is", "awesome","good"]

def upper_string(x):
    return x.upper()

res_2 = map(upper_string, l2)
list_res_2 = list(res_2)
print(list_res_2)

# filter even numbers with filter
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res_3 = filter(lambda x:x % 2 == 0, l3)
list_res_3 = list(res_3)
print(list_res_3)

# Get Words Starting with "a"
def a_words(x):
    return x.startswith("a")

l4 = ["hello", "yes", "apple", "aim"]
res_4 = filter(a_words, l4)
list_res_4 = list(res_4)
print(list_res_4)

# convert to Fahrenheit
l5 = [0, 10, 20, 30, 40]

res_5 = map(lambda x: x * 9/5 + 32, l5)
list_res_5 = list(res_5)
print(list_res_5)

# positive numbers with filter
def positive_numbers(x):
    return x > 0

l6 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

res_6 = filter(positive_numbers, l6)
list_res_6 = list(res_6)
print(list_res_6)

# multipal lists
l7 = [1, 2, 3, 4, 5]
l8 = [2, 0, 2, 4, 6]

res_7 = map(lambda x,y: x * y, l7, l8)
list_res_7 = list(res_7)
print(list_res_7)

# Palindromes
l9 = ["madam", "radar", "hello", "level"]

res_9 = filter(lambda x: x == x[::-1], l9)
list_res_9 = list(res_9)
print(f"input list is {l9}")
print(list_res_9)