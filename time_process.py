import time

def measure_time(func):
	def wrapper(*args, **kwargs):
		print("this is decorator")
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"{func.__name__} took {end - start:.4f} seconds")
		return result
	return wrapper

@measure_time
def sum_numbers():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

print(sum_numbers())


# define func in another function
def outer_func():
    print("this is outer function")
    def inner_func():
        print("this is inner function")
        return "This is return of inner func"
    return inner_func

outer_func_my = outer_func
print(outer_func_my)

inner_func_my = outer_func()
print(inner_func_my)

# func calls another func
def foo():
    print("this is foo function")

def bar(foo_func):
    print(f"this is bar function and {foo_func.__name__} is called")
    foo_func()

print(bar(foo))