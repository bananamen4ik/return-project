import asyncio


# async def hello():
#     await asyncio.sleep(1)
#     return "Hello"
#
#
# async def main():
#     task = asyncio.create_task(hello())
#
#     print(task)
#
#     result = await task
#
#     print(result)
#
#
# asyncio.run(main())

# Что представляет собой task? Объект Task
# Почему print(task) не выводит "Hello"? Потому что ссылка на объект Task. Чтобы получить результат
# нужно дождаться выполнения Task через await надежно
# 1. Что делает await task? Ожидает выполнения Task и возвращает результат корутины

async def first():
    print("first start")
    await asyncio.sleep(1)
    print("first end")
    return 1


async def second():
    print("second start")
    await asyncio.sleep(1)
    print("second end")
    return 2


#
# async def main():
#     task1 = asyncio.create_task(first())
#     task2 = asyncio.create_task(second())
#
#     result1 = await task1
#     result2 = await task2
#
#     print(result1, result2)

# До запуска напиши предполагаемый порядок вывода.
# print("first start"), print("second start"), print("first end"), print("second end"), print(result1, result2)

# примерно сколько секунд будет выполняться программа?
# 1 секунду

# async def main():  # A
#     await first()
#     await second()
#
#
# async def main():  # B
#     task1 = asyncio.create_task(first())
#     task2 = asyncio.create_task(second())
#
#     await task1
#     await task2

# Сколько примерно занимает A? - 2 секунды
# Сколько примерно занимает B? - 1 секунда
# Почему результат разный?
# Потому что в А синхронно ждет программа выполнения поочередного await.
# Во втором случае создаются один за другим через task корутины и выполняются примерно параллельно

# async def foo():
#     print("foo")
#     await asyncio.sleep(1)
#     print("foo done")


# async def main():
#     print("A")
#
#     task = asyncio.create_task(foo())
#
#     print("B")
#
#     await task
#
#     print("C")

# Порядок: print("A"), print("foo"), print("B"), print("foo done"), print("C")
# И объясни, почему foo не обязательно печатает что-либо прямо внутри create_task().
# Этот момент я не понял, я думал что asyncio.create_task(foo()) выполняет код до await внутри foo

# async def foo():
#     return 42
#
#
# async def main():
#     task = asyncio.create_task(foo())
#
#     result = await task
#
#     print(result)  # 42
#     print(task.done())  # True
#     print(task.result())  # 42

# async def foo():
#     await asyncio.sleep(1)
#     return 42
#
#
# async def main():
#     task = asyncio.create_task(foo())
#
#     print(task.done())  # False потому что еще не выполнилась корутина, там секунда пройти должна, а этот участок точно быстрее ее начнется
#
#     await task
#
#     print(task.done())  # True потому что после await гарантировано корутина уже выполнилась

# Разница между coroutine = foo() и task = asyncio.create_task(foo()) и result = await foo()
# coroutine = foo() - получает объект корутины
# task = asyncio.create_task(foo()) - получает объект Task для дальнейшего отслеживания выполнения корутины
# result = await foo()  - дожидается выполнения корутины и получает результат

# async def
#    ↓
# foo()
#    ↓
# Coroutine
#    ↓
# create_task(...)
#    ↓
# Task
#    ↓
# await
#    ↓
# Coroutine value

async def worker(name):
    print(f"{name}: start")
    await asyncio.sleep(2)
    print(f"{name}: end")


async def main():
    task1 = asyncio.create_task(worker("A"))
    task2 = asyncio.create_task(worker("B"))
    task3 = asyncio.create_task(worker("C"))

    await task1
    await task2
    await task3

# Какой будет порядок start? A, B, C
# Какой будет порядок end? A, B, C
# Сколько примерно секунд? 2
# Почему await task1 первым не заставляет task2 и task3 ждать своего запуска?
# Потому что уже все запустились, await task1 лишь ждет конца выполнения своей задачи в не зависимости от других