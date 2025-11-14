# 1
def even_numbers(n):
	number = 0
	while number <= n:
		if number % 2 == 0:
			yield number
		number += 1
        
for num in even_numbers(20):
    print(num)


# 2
even_numbers_generator = (num for num in range(1, 21) if num % 2 == 0)
for num in even_numbers_generator:
    print(num)

# 3 words
def word_generator(sentence):
	words = sentence.split()
	for word in words:
		yield word

for word in word_generator("hello world"):
	print(word)

# 4
def number_generator(n):
	for i in range(1,n+1):
		yield i
print("task 4")

for num in number_generator(5):
	print(num)

# 5
print("task 5")

def squared(gen):
	for num in gen:
		yield num * num

for num in squared(number_generator(5)):
	print(num)

