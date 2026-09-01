import asyncio


async def hello():
    return "Hello"


async def main():
    print(await hello())


asyncio.run(main())

async def get_number():
    return 42


async def main():
    result = await get_number()
    print(result)
    print(type(result))


asyncio.run(main())

async def first():
    print("first")
    return 1


async def second():
    print("second")
    return 2


async def main():
    a = await first()
    b = await second()

    print(a, b)


asyncio.run(main())

# После запуска будет print("first"), return 1, print("second"), return 2, print(a, b)


async def first():
    print("first start")
    await asyncio.sleep(1)
    print("first end")


async def second():
    print("second start")
    await asyncio.sleep(1)
    print("second end")


async def main():
    await first()
    await second()

#  После запуска займет примерно 2 секунды из-за двух asyncio.sleep которые приостанавливают выполнение

async def foo():
    return 10

result = foo()

print(result)
print(type(result))

# Что находится в result? - Находится courutine object
# Почему там не 10? - Потому что не вызывается с помощью await который начинает выполнение
# Выполнялась ли foo()?  Нет, только создан объект корутины

async def main(): # нужно было добавить async, так как await может использоваться только в асинхронном контексте
    result = await get_data()
    print(result)

# def foo(): отличается от async def foo():, тем, что это обычная функция и при вызове она сразу выполняется
# а async создает корутину и ждем await чтобы выполниться асинхронно

# foo() вернет coroutine object, если объявлена с помощью async

# await foo() выполняет функцию корутину

# asyncio.run(main()) нужен чтобы запустить выполнение верхней корутины, я так понимаю запускатеся event loop

async def foo():
    print("A")
    await asyncio.sleep(1)
    print("B")


async def main():
    print("C")
    await foo()
    print("D")


asyncio.run(main())

# Запускается main(), print("C"), print("A"), ожидание 1 сек, print("B"), print("D")
# Будет порядок: C, A, B, D. Такой порядок из-за вызовов выше