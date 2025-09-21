a, b = 5, 10
print(a,b)
a, b = b, a
print(a,b)

point = (4, 5, 6)
x,y,_ = point
print(x,y)

def f1(sum,product):
    return (sum,product)

sum,product = f1(10,200)
print(sum,product)

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
for num,word in pairs:
    print(f"{num} is {word}")

nums = (1, 2, 3, 4, 5)
a,*middle,b = nums
print(a,middle,b)

student = ("Alice", (90, 85, 92))
name,(math,science,english) = student
print(name,math,science,english)

mylist = [(1,2), (3,4), (55,66)]
for a,b in mylist:
      print(a)
      print(a+b)

students = [("Alice", 85), ("Bob", 72), ("Charlie", 90), ("Diana", 60)]
l1 = [name for name,score in students if score > 75]
print(l1)