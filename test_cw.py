import time
def print_decorator(func):
    def wrapper(*arqs, **kwarqs):
        start_time = time.time()
        result = func(*arqs, **kwarqs)
        print(time.time() - start_time)
        return result
    return wrapper

@print_decorator
def print_hello():
    print("hello")

print(print_hello())

@print_decorator
def sum(num_1: int, num_2: int):
    return num_1 + num_2

print(sum(3, 5))

# print_hello = lambda : print("hello")
# print_hello()