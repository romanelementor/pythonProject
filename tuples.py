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
    