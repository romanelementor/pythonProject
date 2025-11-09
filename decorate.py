def uppercase_output(func):
    def wrapper(*args, **kwargs):
        print("this is decorator")
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_output
def greeting():
    return "Hello, world!"

print(greeting())
