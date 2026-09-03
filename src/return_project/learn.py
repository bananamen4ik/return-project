import asyncio


async def numbers():
    yield 1
    yield 2
    yield 3


async def main():
    async for number in numbers():
        print(number)


# Напечатает 1, 2, 3
# И объясни, почему здесь используется async for, а не обычный for. - Потому что numbers async generator


async def numbers():
    for number in range(5):
        await asyncio.sleep(1)
        yield number


async def main():
    async for number in numbers():
        print(number)


asyncio.run(main())

# 3
async def events():
    while True:
        event = await get_event()
        yield event

# await get_event()
#         ↓
# evenv loop wait get_event
#         ↓
# yield event
#         ↓
# async for получает event, асинхронный генератор events приостанавливается

# 4
async def foo():
    return [1, 2, 3]

async def foo():
    yield 1
    yield 2
    yield 3

# Разница между ними в том, что первая функция это корутина, вторая же асинхронный генератор

# Что возвращает вызов foo() в каждом случае и как эти результаты получать?
# Первый: объект корутины, получить правильно await foo() для результата
# Второй: объект асинхронного генератора, правильно получить результаты async for x in foo()
