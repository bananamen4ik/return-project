from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    name: str
    email: str | None


user = User(
    id=1,
    name="Armen",
    email=None,
)

print(user)


# Объясни, какие методы dataclass сгенерировал автоматически.
# __repr__, __init__ и другие

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)


a = User("A")
b = User("B")

a.tags.append("python")


# Что произойдёт? У меня ValueError когда пытаюсь mutable [] напрямую назначить полю tags, но по идее тогда все бы
# экземпляры имели общий объект
# Когда field используются у всех в момент создания отдельные объекты mutable

# Разница между str | None и str в том, что в первом случае ожидает str или None, во втором только str
# И ответь, означает ли: age: int что Python обязательно выбросит ошибку, если передать строку.
# Он не проверяет типы которые передаются в момент выполнения программы и до выполнения. Это лишь для инструментов
# IDE, и других на проверку типов кода

# 4
# users: list[str] - ожидается список с str элементами
# users: dict[int, str] - ожидается словарь где ключ int, значение str
# users: Iterable[str] - любой итерируемый объект с str значением
# Особенно объясни, чем Iterable[str] отличается от list[str]. iterable любой итерируемый объект с str значением,
# list - именно список с str значением

# 5
# Callable[[int, str], bool]
# Что должна принимать такая функция и что возвращать?
# Принимает два аргумента, первый int, второй str, возвращает bool

# Подходящая функция к примеру:
def ex(num: int, name: str) -> bool:
    return True


# 6
from dataclasses import dataclass
from collections.abc import Iterable, Callable


@dataclass
class Service:
    id: int
    name: str
    price: float
    description: str | None
    tags: list[str]


def find_services(
        services: Iterable[Service],
        predicate: Callable[[Service], bool],
) -> list[Service]:
    return [service for service in services if predicate(service)]


def predicate(service: Service) -> bool:
    return service.description is not None


service1 = Service(
    id=1,
    name="Service 1",
    price=10,
    description="Service 1",
    tags=["tag1", "tag2"],
)

service2 = Service(
    id=2,
    name="Service 2",
    price=20,
    description=None,
    tags=["tag1", "tag2"],
)

services = [service1, service2]

print(find_services(services, predicate))
