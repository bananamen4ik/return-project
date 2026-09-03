import asyncio
from contextvars import ContextVar

user_id = ContextVar("user_id")


async def worker(name, value):
    user_id.set(value)
    await asyncio.sleep(0.1)
    print(name, user_id.get())


async def main():
    await asyncio.gather(
        worker("A", 100),
        worker("B", 200),
    )


asyncio.run(main())


async def main():
    user_id.set(10)
    print(user_id.get())
    token = user_id.set(20)
    print(user_id.get())
    user_id.reset(token)
    print(user_id.get())


asyncio.run(main())

import inspect


def normal():
    pass


async def async_func():
    pass


async def async_generator():
    yield 1


print(inspect.isfunction(normal))
print(inspect.iscoroutinefunction(async_func))
print(inspect.isasyncgenfunction(async_generator))


def create_user(name: str, age: int = 18, active: bool = True):
    pass


for name, param in inspect.signature(create_user).parameters.items():
    print(name, param.default, param.annotation)

from typing import Protocol


# 5
class Storage(Protocol):
    def save(self, data: str) -> None:
        ...


class FileStorage:
    def save(self, data: str) -> None:
        print(data)


class DatabaseStorage:
    def save(self, data: str) -> None:
        print(data)


def save_data(storage: Storage, data: str):
    storage.save(data)


save_data(FileStorage(), "file")
save_data(DatabaseStorage(), "db")

# 1. Чем ContextVar отличается от глобальной переменной? В каждом контексте выполнения функции будет своя область видимости, в глобальной вся программа видит ее
# 2. Для чего нужен inspect? Чтобы во время выполнения получить информацию о сигнатуре объекта или функции, информация параметров, тип и тд
# 3. Чем Protocol отличается от обычного наследования? Protocol нужен чисто для статической типизации без наследования, обычное наследование на уровне программы и наследования
# 4. В чём концептуальная разница между ABC и Protocol? В наследовании
