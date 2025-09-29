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

str = "hello world"
print(str.split())
print(f"first 4 characters are {str[:4]}")
print(f"last 4 characters are {str[-4:]}")
print(f"every 2nd character even are {str[::2]}")
print(f"every 2nd character odd are {str[1::2]}")
print(f"every 2nd character in reverse are {str[::-2]}")

l10 = [1, 2, 3, 4, 5, 6]
res_10 = filter(lambda x:x % 2 == 0, l10)
l11 = list(res_10)
res_11 = map(lambda x: x *2 , l11)
l12 = list(res_11)
print(l12)

#ver2
l13 = list(map(lambda x: x *2 ,filter(lambda x:x % 2 == 0, l10)))
print(l13)

l14 = ["hi", "world", "map", "filter"]
l15 = list(map(lambda x: len(x), filter(lambda x: len(x)> 3, l14)))
print(l15)

def myfunc(*args):
    return list(filter(lambda x:x % 2 == 0,args))

print(myfunc(5,6,7,8))

def myfunc(s):
    l = []
    for i in range(len(s)):
        if i % 2 == 0:
            l.append(s[i].lower())
        else:
            l.append(s[i].upper())
    return "".join(l)

print(myfunc("Anthropomorphism"))

def maxNumber(*args):
    return max(args)

print(maxNumber(1,2,31,7,5))

def strConcate(*args):
    return " ".join(args)

print(strConcate("hello", "world", "python", "is", "awesome"))

def reverseString(s):
    return s[::-1]

print(reverseString("hello"))

def numMultip(*args):
    l20 = list(args)
    result = 1
    for i in range(len(l20)):
        result = result * l20[i]

    return result

print(numMultip(2,3,4))

def paper_doll(text):
    result = ""
    for i in range(len(text)):
        result = result + text[i]*3
    return result

print(paper_doll("hello"))

def polindromfunc(text):
    n = int(len(text)/2)
    for i in range(n):
        if text[i] != text[len(text) - i -1]:
            return False
    return True

print(polindromfunc("level"))

def multiply_all(*args):
    result = 1
    for i in range(len(args)):
        result = result * args[i]

    return result

print(multiply_all(1,2,3,4))

def power_sum(power, *args):
    result = 0
    for i in range(len(args)):
        result = result + args[i] ** power

    return result

print(power_sum(2,1,2,3))

def greet(greeting, *names):
    for name in names:
        print(f"{greeting} {name}")

print(greet("Hello", "Alice", "Bob", "Charlie"))

def avg_num(*args):
    return sum(num for num in args)/len(args)

print(avg_num(1,2,3,4,5))