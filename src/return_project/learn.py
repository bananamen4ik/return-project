import asyncio


async def worker(name, delay):
    await asyncio.sleep(delay)
    return name


async def main():
    tasks = [
        asyncio.create_task(worker("A", 3)),
        asyncio.create_task(worker("B", 1)),
        asyncio.create_task(worker("C", 2)),
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

    # порядок: B, C, A
    # время: 3


asyncio.run(main())

tasks = [
    asyncio.create_task(worker("A", 1)),
    asyncio.create_task(worker("B", 3)),
    asyncio.create_task(worker("C", 2)),
]

for task in asyncio.as_completed(tasks):
    print(await task)


# вывод: A, C, B
# общее время: 3

#
async def a():
    await asyncio.sleep(3)
    return "A"


async def b():
    await asyncio.sleep(1)
    return "B"


async def c():
    await asyncio.sleep(2)
    return "C"


#
results = await asyncio.gather(
    a(),
    b(),
    c(),
)
print(results)

#
tasks = [
    asyncio.create_task(a()),
    asyncio.create_task(b()),
    asyncio.create_task(c()),
]

for task in asyncio.as_completed(tasks):
    print(await task)

# gather:
# результат: ["A", "B", "C"]
# время: 3
#
# as_completed:
# порядок вывода: B, C, A
# время: 3

# 4
async def request(name, delay):
    print(f"{name}: start")
    await asyncio.sleep(delay)
    print(f"{name}: end")
    return name

tasks = [
    asyncio.create_task(request("A", 3)),
    asyncio.create_task(request("B", 1)),
    asyncio.create_task(request("C", 2)),
]

for task in asyncio.as_completed(tasks):
    result = await task
    print("RESULT:", result)

# Вывод:
# A start, B start, C start, B end, RESULT: B, C end, RESULT: C, A end, RESULT: A

# 5
tasks = [
    asyncio.create_task(request("Google", 3)),
    asyncio.create_task(request("Bing", 1)),
    asyncio.create_task(request("DuckDuckGo", 2)),
]

# выберу as_completed, так как он позволяет получать результаты по мере выполнения корутин

# 6
async def good(name, delay):
    await asyncio.sleep(delay)
    return name


async def bad():
    await asyncio.sleep(1)
    raise ValueError("error")

tasks = [
    asyncio.create_task(good("A", 3)),
    asyncio.create_task(bad()),
    asyncio.create_task(good("C", 2)),
]

for task in asyncio.as_completed(tasks):
    result = await task
    print(result)

# Какая Task завершится первой? bad
# Что произойдёт на await task для неё? выдано исключение
# Будут ли остальные Tasks автоматически отменены? да
# Что произойдёт с A и C? отменятся

# Разница между await asyncio.gather(...) и await asyncio.wait(...) и asyncio.as_completed(...):
# gather — ждет пока выполнятся все корутины
#
# wait — есть возможность настроить когда получить результат с помощью условия и контролировать выполнение с помощью done, pending
#
# as_completed — отдает корутины по мере их выполнения