import asyncio


async def get_number(number):
    await asyncio.sleep(1)
    return number

async def main():
    results = await asyncio.gather(
        get_number(1),
        get_number(2),
        get_number(3),
    )

    print(results)  # [1, 2, 3]

# results тип list, займет 1 секунду

async def first():
    await asyncio.sleep(3)
    return "first"


async def second():
    await asyncio.sleep(1)
    return "second"


async def third():
    await asyncio.sleep(2)
    return "third"

results = await asyncio.gather(
    first(),
    second(),
    third(),
)

print(results)

# results = ["first", "second", "third"]
# время ≈ 3
# в каком порядке фактически завершатся coroutine? - second, third, first

async def get_name():
    await asyncio.sleep(1)
    return "Armen"


async def get_age():
    await asyncio.sleep(1)
    return 27


async def get_city():
    await asyncio.sleep(1)
    return "Amsterdam"


async def main():
    name, age, city = await asyncio.gather(
        get_name(),
        get_age(),
        get_city(),
    )

    print(name, age, city)


asyncio.run(main())

# Объясни, почему здесь порядок переменных не зависит от того, какая coroutine завершилась первой.
# Потому что gather отдает элементы в списке такой же последовательности, какой аргументы были переданы в него

# A
task1 = asyncio.create_task(first())
task2 = asyncio.create_task(second())

result1 = await task1
result2 = await task2

# B
result1, result2 = await asyncio.gather(
    first(),
    second(),
)

# Будет ли разница во времени выполнения? Не будет
# Что в итоге делает gather()? Помогает запускать без лишнего кода удобно конкурентно корутины и получать результаты
# Что получаем в result1 и result2? "first" и "second"
# Нужно ли нам вручную создавать Tasks в варианте B? Нет

async def foo():
    await asyncio.sleep(1)
    return 10


async def bar():
    await asyncio.sleep(2)
    return 20


async def main():
    results = await asyncio.gather(foo(), bar())

    print(results)
    print(type(results))

# вывод: [10, 20]
# тип: list
# время: 2

async def good():
    await asyncio.sleep(1)
    return "OK"


async def bad():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong")

async def main():
    results = await asyncio.gather(
        good(),
        bad(),
    )

    print(results)

# Вернётся ли results? Я так понимаю исключение пойдет вверх и программа завершится
# Что произойдёт с ValueError? Пробьется наружу и остановит выполнение программы
# Напечатается ли results? Нет
# 1. Что произойдёт с good()? Выполнится полностью

results = await asyncio.gather(
    good(),
    bad(),
    return_exceptions=True,
)  # results = ["OK", ValueError("Something went wrong")]

async def request(name, delay):
    print(f"{name}: start")
    await asyncio.sleep(delay)
    print(f"{name}: end")
    return name

results = await asyncio.gather(
    request("A", 3),
    request("B", 1),
    request("C", 2),
)

# 1. Порядок start? A, B, C
# 2. Порядок end? B, C, A
# 3. Что будет в results? ["A", "B", "C"]
# 4. Сколько секунд? 3
# 5. Почему порядок end и порядок results будут различаться?
# Потому что порядок results зависит от порядка аргументов в gather, а end от времени sleep

foo()
create_task(foo())
await foo()
await asyncio.gather(foo(), bar())

# Coroutine -> Task -> result coroutine -> result 2 coroutines