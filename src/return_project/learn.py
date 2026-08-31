def greet(name):
    return f"Hello, {name}"


say_hello = greet
print(say_hello("Armen"))

def apply(func, value):
    return func(value)


def double(number):
    return number * 2


print(apply(double, 10))

square = lambda x: x ** 2
print(square(5))

numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x ** 2, numbers)))

users = [
    {"name": "Armen", "age": 27},
    {"name": "John", "age": 30},
    {"name": "Alex", "age": 25},
    {"name": "Maria", "age": 22},
]

print(sorted(users, key=lambda x: x["age"]))
print(sorted(users, key=lambda x: len(x["name"])))

def apply_operation(func, a, b):
    return func(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(apply_operation(add, 10, 5))  # 15
print(apply_operation(multiply, 10, 5))  # 50

def make_multiplier(multiplier):
    def multiply(x):
        return x * multiplier

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

# count не сбрасывается так как counter один и тот же объект в котором
# сохранена переменная count замыканием и с ней происходит взаимодействие каждый раз при вызове