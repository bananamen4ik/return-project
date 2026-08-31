def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)

    return wrapper


@log_call
def greet():
    print("Hello")


greet()


def around(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")

        return result

    return wrapper


@around
def greet():
    print("Hello")


greet()


def log_call(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@log_call
def greet(name):
    return f"Hello, {name}"


result = greet("Armen")
print(result)


def log_call(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def introduce(name, age):
    return f"{name}: {age}"


print(add(1, 2))
print(introduce("Armen", 27))

from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@log_call
def greet():
    """Greeting function."""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)

from functools import wraps


def log_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_result
def add(a, b):
    return a + b


result = add(10, 20)
print(result)

from functools import wraps


def repeat(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello():
    print("Hello")


hello()


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b

# Здесь функция add к которой применяется декоратор decorator. При запуске add по сути выполняется
# wrapper (если еще углубиться, то вызывается внутренняя функция декоратора wraps который готовит
# необходимые метаданные исходной функции. И в итоге выводится Before, затем вызывается исходная функция
# add, значение записывается в result, выводится After и result возвращается.
# Ответ на вопрос: "почему wrapper всё ещё может вызвать исходный add, хотя decorator() уже завершилась."
# Потому что add переменная после замыкания которую помнит wrapper
