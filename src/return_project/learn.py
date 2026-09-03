# Разница между with resource(): и async with resource():
# В том, что первый это синхронный context manager, второй асинхронный
# И какие методы используются внутри обычного и async context manager:
# И там, и там yield, внутри второго еще: await

# 2
from contextlib import asynccontextmanager


@asynccontextmanager
async def resource():
    print("open")

    try:
        yield "hello"
        print("after yield")
    finally:
        print("cleanup")


async def main():
    async with resource() as value:
        print(value)


# Напечатает: open, hello, after yield, cleanup
# почему after yield выполняется после тела async with: потому что после завершения async with блока
# происходит exit, который выполняет оставшийся код в контекстном менеджере

# 3
import asyncio


@asynccontextmanager
async def connection():
    print("connect")
    await asyncio.sleep(1)

    try:
        yield "connection"
    finally:
        print("close")


async def main():
    async with connection() as conn:
        print(conn)


asyncio.run(main())


# 4
async def main():
    try:
        async with resource():
            print("inside")
            raise ValueError("boom")
    except ValueError:
        print("caught")


# Что произойдёт здесь? Произойдет исключение которое обработается внешним ValueError, при этом resource правильно завершиться с finally.
# Порядок будет: open, inside, cleanup, caught
# И почему cleanup всё равно выполняется? Потому что finally выполняется в любом случае

# 5
@asynccontextmanager
async def resource():
    resource = await acquire()

    try:
        yield resource
    finally:
        await release(resource)

# Объяснение конструкции:
# resource() - это асинхронный контекстный менеджер, aenter: код до yield, aexit все что после

# Мне особенно интересно, чтобы ты объяснил роль await, yield и finally отдельно.
# await ожидает acquire результат и передает управление event loop
# yield возвращает значение в async with
# finally служит cleanup, который выполнится даже если произойдет внутри async with исключение
