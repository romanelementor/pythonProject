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