try:
    raise ExceptionGroup(
        "test",
        [
            ValueError("value"),
            TypeError("type"),
        ],
    )
except* ValueError:
    print("value caught")

# Выведется print("value caught") и далее вылезет наружу TypeError("type")
# Выведется ли value caught? да
# Что произойдёт с TypeError? вылезет наружу
# Завершится ли программа без необработанного исключения? нет

try:
    raise ExceptionGroup(
        "test",
        [
            ValueError("value"),
            TypeError("type"),
        ],
    )
except* ValueError:
    print("value caught")
except* TypeError:
    print("type caught")

# Будет выведено: print("value caught"), print("type caught")

try:
    raise ExceptionGroup(
        "test",
        [
            ValueError("A"),
            TypeError("B"),
            ValueError("C"),
        ],
    )
except* ValueError as e:
    print("caught:", type(e))
    print("number:", len(e.exceptions))

# какой будет type(e)? ExceptionGroup
# чему будет равен len(e.exceptions)? 2
# какие именно исключения окажутся внутри e? ValueError

import asyncio


async def worker(name, exc):
    await asyncio.sleep(1)
    raise exc


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(worker("A", ValueError("A error")))
            tg.create_task(worker("B", TypeError("B error")))
    except* ValueError:
        print("value")
    except* TypeError:
        print("type")


asyncio.run(main())

# Что произойдёт с TaskGroup? вызовется ValueError("A error"), отменится worker B, и print("value")
# Но это с учетом что worker B не успеет завершиться сам, но так как там и там 1 секунда выполнения,
# то я предпологаю он тоже может завершиться и то CancelledError он выкенет свой TypeError и тогда и его ошибка обработается
# Почему здесь можно использовать два except*? потому что отдельно обрабатываются две ошибки
# Что выведется? print("value")
# Будут ли ValueError и TypeError существовать как два отдельных исключения, или наружу выйдет ExceptionGroup?
# выйдет ExceptionGroup

# 5
async with asyncio.TaskGroup() as tg:
    tg.create_task(worker("A", ValueError("A")))
    tg.create_task(worker("B", TypeError("B")))

# A → ValueError добавляются в очередь
# B → TypeError добавляются в очередь
#       ↓
# TaskGroup вызывает
#       ↓
# ExceptionGroup обе ошибки перехватываются и добавляются в группу исключений
#       ↓
# except* ValueError по отдельности обрабатываются
# except* TypeError по отдельности обрабатываются

# Почему TaskGroup вообще нужен ExceptionGroup, если обычный except уже умеет ловить исключения?
# Потому что может во время работы перехватиться не одна ошибка, а несколько

# 6
# Сравнить except ValueError:  и except* ValueError:
# except работает с одним исключением, а except* отбирает конкретные типы исключений из группы
