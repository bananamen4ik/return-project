from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int


product = Product("MacBook", 2000, 2)

print(product)

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int
    is_available: bool = True


product = Product("MacBook", 2000, 2)
print(product)
product = Product("MacBook", 2000, 2, False)
print(product)

from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    skills: list[str] = field(default_factory=list)


user1 = User("Armen")
user2 = User("John")

user1.skills.append("Python")

print(user1)
print(user2)


def calculate_total(price: float, quantity: int, discount: float) -> float:
    ...


def get_user(user_id: int) -> dict[str, str | int] | None:
    ...


# Означает что функция принимает user_id integer и возвращает либо (словарь где ключ это str, значение str или int), либо None

from collections.abc import Iterable

numbers: list[int] = [1, 2, 3, 4, 5]


def get_even_numbers(numbers: Iterable[int]) -> list[int]:
    ...


from collections.abc import Callable


def apply_operation(func: Callable[[int], int], number: int) -> int:
    return func(number)


def square(x: int) -> int:
    return x ** 2


print(apply_operation(square, 5))
#
# Разница между list[int], Iterable[int] и Iterator[int] в том что:
# list[int] ожидается list с элементами int
# Iterable[int] любой объект, у которого есть итератор и по нему можно пройтись и вернет int
# Iterator[int] напрямую ожидается итератор который возвращает int
#
# почему list[int] уже конкретная структура данных, а Iterable[int] описывает более широкий набор объектов?
# Потому что Iterable может выступать множество разных структур данных у которых есть итератор, а list это одна из

from dataclasses import dataclass, field
from collections.abc import Iterable


@dataclass
class User:
    id: int
    name: str
    age: int
    skills: list[str] = field(default_factory=list)
    is_active: bool = True


def get_active_users(users: Iterable[User]) -> list[User]:
    return list(users)


user1: User = User(1, "Armen", 27, skills=["Python", "Django"])
user2: User = User(2, "John", 30)

print(get_active_users((user1, user2)))


@dataclass
class User:
    name: str
    skills: list[str] = field(default_factory=list)


user1 = User("Armen")
user2 = User("John")

user1.skills.append("Python")

print(user1.skills)  # ["Python"]
print(user2.skills)  # []

# И почему здесь default_factory=list, а не просто skills: list[str] = []?
# Потому что list это mutable коллекция и чтобы не сделать для всех единый список есть специальная функция field
