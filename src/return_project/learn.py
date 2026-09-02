import asyncio


async def worker(name, delay):
    await asyncio.sleep(delay)
    return name


async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(worker("A", 3))
    task2 = tg.create_task(worker("B", 1))
    task3 = tg.create_task(worker("C", 2))

# 1. Сколько примерно времени? 3
# 2. Все ли Tasks завершатся? да
# 3. Что будет после async with? все задачи завершатся и программа продолжит работу
# 4. Что вернёт task1.result()? A

async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(worker("A", 3))
    task2 = tg.create_task(worker("B", 1))
    task3 = tg.create_task(worker("C", 2))

print(task1.result())
print(task2.result())
print(task3.result())


# Вывод будет: A, B, C с каждой новой строки как print идет

async def good(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def bad():
    await asyncio.sleep(1)
    raise ValueError("error")


try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(good("A", 3))
        tg.create_task(bad())
        tg.create_task(good("C", 2))
except* ValueError:
    print("caught")

# Что произойдёт через 1 секунду? Вызовется ValueError("error")
# Успеет ли A вывести A finished? Нет
# Успеет ли C вывести C finished? Нет
# Что будет выведено после TaskGroup? print("caught")
# Будут ли A и C отменены? Да

# 4
async def good(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return name


async def bad():
    await asyncio.sleep(1)
    raise ValueError("error")

# A
await asyncio.gather(
    good("A", 3),
    bad(),
    good("C", 2),
)

# B
async with asyncio.TaskGroup() as tg:
    tg.create_task(good("A", 3))
    tg.create_task(bad())
    tg.create_task(good("C", 2))

# Что принципиально произойдёт с A и C при ошибке bad() в каждом варианте?
# В варианте A: выполнятся и попадут в list
# В варианте C: отменятся

async with asyncio.TaskGroup() as tg:
    tg.create_task(worker("A", 1))
    tg.create_task(worker("B", 2))

# Этот код не позволяет написать results = await ... как с gather, потому что здесь нужно сохранить
# результаты в переменные и после async with получить результаты через .result()

async def worker(name):
    try:
        await asyncio.sleep(10)
        print(name)
    except asyncio.CancelledError:
        print(f"{name} cancelled")
        raise

try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("A"))
        tg.create_task(worker("B"))

        await asyncio.sleep(1)
        raise ValueError("boom")
except* ValueError:
    print("caught")

# Полный вывод, здесь я напишу как я вижу, но нужна будет помощь:
# Сначала вызовется raise ValueError("boom"), затем A cancelled, B cancelled, print("caught")
# но не знаю что будет с двумя asyncio.CancelledError которые пробрасываются наружу когда конкретно завершится программа

# 7
# gather - выполнить корутины и вернуть результаты в list
# TaskGroup - сгруппировать таски, поставить на выполнение и автоматически отменить в случае ошибки одного из

# 8
# Нужно одновременно:
# - получить пользователя из PostgreSQL
# - получить настройки из Redis
# - запросить данные внешнего API

# я бы выбрал gather, так как в случае ошибки он не прервет оставшиеся задачи и вернет все результаты в том числе и errors
