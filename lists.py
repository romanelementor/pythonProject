print("lists")

list1 = [x for x in range(1,11)]
print(list1)

list2 = [x* x for x in list1]
print(list2)

list3 = [x for x  in list1 if x % 2 == 0]
print(list3)

list4 = ["python", "is", "awesome"]
list5 = [len(x) for x in list4]
print(list5)

list6 = [[1,2,3],[4,5,6],[7,8,9]]
list7 = [x for sublist in list6 for x in sublist]
print(f"flatten list is {list7}")

list8 = ["even" if x % 2 == 0 else x for x in list1]
print(f"list8 evens is {list8}")

sentence = "List comprehension makes Python powerful"
list9 = [x[0] for x in sentence.split()]
print(f"list9 sentence is {list9}")

word = "comprehension"
list10 = [x for x in word if x in ("a", "e", "i", "o", "u")]
print(f"list10 vowels is {list10}")

list11 = [x for x in range(1,21) if x % 2 == 0 or x % 5 == 0]
print(f"list11 divisible by 2 or 5 is {list11}")

fruits = ["apple", "banana", "cherry"]
list12 = [(x,len(x)) for x in fruits]
print(f"list12 fruits is {list12}")

list13 = [1,2,3,4,5,0,0,7,0,9,0]
print(list13[0])
y = list13[2]

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(f"unique_list is {unique_list}")