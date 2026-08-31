class User:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, value: str):
        value_parts = value.split(",")
        return cls(value_parts[0], int(value_parts[1]))


user = User.from_string("Armen,27")
print(user.name, user.age)


class User:

    @classmethod
    def create(cls):
        return cls()


class Admin(User):
    pass


user = Admin.create()  # Вернется экземпляр Admin

print(type(user))  # Admin, так как cls смотрит текущий класс который вызывается


class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MathUtils.is_even(10))  # True
print(MathUtils.is_even(7))  # False

user.get_full_name() - обычный
метод
User.from_string("Armen,27") - classmethod
User.calculate_something(10, 20) - staticmethod


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


user = User("Armen", "Doe")

print(user.full_name)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price


product = Product(100)
product.price = -100
print(product.price)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"


user = User("Armen", 27)
print(user)
print(repr(user))


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

    @property
    def is_adult(self):
        return self.age >= 18


user = User.from_string("Armen,27")
print(user)

# user.greet() отличается тем что вызывается экземпляр и работа происходит с self
# User.from_string(...) здесь доступ есть только к cls если используется classmethod
# User.is_something(...) если реализовано через staticmethod, то нет доступа к self и cls

# Когда тебе нужен self, когда cls, а когда вообще ничего не нужно?
# self если нужно взаимодействие с данными экземпляра, cls если только доступ к классу, если ни то, ни другое то staticmethod
