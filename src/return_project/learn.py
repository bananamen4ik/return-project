class MyContext:
    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")


with MyContext():
    print("Inside")


class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with MyContext() as context:
    print(context)


class MyContext:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Error:", exc_val)


with MyContext():
    raise ValueError("Something went wrong")


class IgnoreErrors:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


with IgnoreErrors():
    raise ValueError("Boom")

print("Continues")

from contextlib import contextmanager


@contextmanager
def my_context():
    print("Enter")
    try:
        yield
    finally:
        print("Exit")


with my_context():
    print("Inside")

from contextlib import contextmanager


@contextmanager
def managed_resource():
    value = "Resource"
    print(value, "acquired")
    yield value
    print(value, "released")


with managed_resource() as resource:
    print(resource)


class Test:
    def __enter__(self):
        print("1")
        return "hello"

    def __exit__(self, exc_type, exc_value, traceback):
        print("4")


with Test() as value:
    print("2")
    print(value)
    print("3")

# Сначала выведется 1, затем 2, hello, 3, 4. То есть сначала enter, затем тело, затем exit.
# 1. Что попадёт в value? В value попадет hello
# 2. Почему __exit__() вызывается после print("3")? Потому что вызывается он только после выполнения тела или при исключении
# 3. Что будет с исключением, если __exit__() вернёт True? Программа продолжится дальше без проброса исключения выше
# 4. 1. Что будет, если вернёт False? Тогда исключения пробросится выше

with open("data.txt") as f:
    data = f.read()
# with лучше, так как надежней в плане что не забудешь закрыть ресурс например,
# меньше повторения кода

# И почему try/finally по смыслу очень близок к тому, что делает context manager?
# так как try/finally смысл схож что в любом случае выполнится блок finally который закроет к примеру ресурс
