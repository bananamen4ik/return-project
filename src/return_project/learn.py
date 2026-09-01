import asyncio


async def worker(name, delay):
    await asyncio.sleep(delay)
    return name


task1 = asyncio.create_task(worker("A", 3))
task2 = asyncio.create_task(worker("B", 1))
task3 = asyncio.create_task(worker("C", 2))

done, pending = await asyncio.wait(
    {task1, task2, task3}
)

# Сколько примерно секунд? 3
# Что будет в pending? set невыполненных task
# Что находится внутри done? set выполненных task
# Что вернёт task1.result()? если после текущей wait написать то A результат выполнения корутины

done, pending = await asyncio.wait(
    {task1, task2, task3},
    return_when=asyncio.FIRST_COMPLETED,
)

# время ≈ 1
# done содержит ? - set(task2)
# pending содержит ? - set(task1, task3)

for task in done:
    print(task.result())  # Будет напечатано: B

# work 4
done, pending = await asyncio.wait(
    tasks,
    return_when=asyncio.FIRST_COMPLETED,
)

done2, pending2 = await asyncio.wait(pending)


# Что находится в done2? set(task1, task3)
# Что находится в pending2? set()
# Сколько примерно времени займёт вся программа? 1 секунда уже прошла, и две секунды займет следующий wait для done2
# Как получить результаты всех Tasks? можно пройтись циклом по done и done2 и вызвать .result() каждого task

async def a():
    await asyncio.sleep(3)
    return "A"


async def b():
    await asyncio.sleep(1)
    return "B"


async def c():
    await asyncio.sleep(2)
    return "C"


# A
results = await asyncio.gather(
    a(),
    b(),
    c(),
)

# B
tasks = {
    asyncio.create_task(a()),
    asyncio.create_task(b()),
    asyncio.create_task(c()),
}

done, pending = await asyncio.wait(
    tasks,
    return_when=asyncio.FIRST_COMPLETED,
)


# A:
# время = 3 секунды
# результат = ["A", "B", "C"]
#
# B:
# время = 1 секунда
# done = set(b)
# pending = set(a, c)

async def good():
    await asyncio.sleep(2)
    return "OK"


async def bad():
    await asyncio.sleep(1)
    raise ValueError("error")


async def main():
    task1 = asyncio.create_task(good())
    task2 = asyncio.create_task(bad())

    done, pending = await asyncio.wait(
        {task1, task2},
        return_when=asyncio.FIRST_EXCEPTION,
    )


# Через сколько примерно wait() вернётся? 1 секунда
# Какая Task будет в done? task2
# Какая в pending? task1
# Что произойдёт, если сделать:
for task in done:
    print(task.result())  # ValueError("error")

# 7
done, pending = await asyncio.wait(
    tasks,
    timeout=1,
)

# A → 5 секунд
# B → 3 секунды
# C → 2 секунды

# через сколько wait вернётся? 1 секунду
# done = set()
# pending = set(a, b, c)
# будут ли pending Tasks автоматически отменены из-за timeout=1? нет

# Разница между await asyncio.gather(...) и await asyncio.wait(...) в возможности получить по мере выполнения task

# Если мне нужно сделать 10 HTTP-запросов и получить результаты всех 10, что естественнее использовать?
# Естественнее gather

# У меня есть 10 Tasks, и мне нужно обработать первую завершившуюся, не дожидаясь остальных?
# Тогда wait
