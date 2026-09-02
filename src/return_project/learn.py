import asyncio

counter = 0
lock = asyncio.Lock()


async def increment(name):
    global counter

    async with lock:
        print(name, "start")

        current = counter
        await asyncio.sleep(1)
        counter = current + 1

        print(name, "end")


async def main():
    await asyncio.gather(
        increment("A"),
        increment("B"),
        increment("C"),
    )

    print(counter)


asyncio.run(main())

# Сколько времени примерно займёт выполнение? 3 секунды
# Что будет выведено относительно start/end? A start, A end, B start, B end, C start, C end
# Какое значение будет у counter? 3
# Почему задачи не выполняют критическую секцию одновременно, несмотря на gather()? lock блокирует остальные таски пока
# не завершится

lock = asyncio.Lock()


async def worker(name):
    print(name, "before")

    async with lock:
        print(name, "inside")
        await asyncio.sleep(2)
        print(name, "after")

    print(name, "outside")


await asyncio.gather(
    worker("A"),
    worker("B"),
)

# Могут ли оба before выполниться подряд? нет
# Могут ли одновременно выполняться A inside и B inside? нет
# Может ли B before выполниться, пока A находится внутри Lock? да
# Когда B сможет войти в Lock? после A after

semaphore = asyncio.Semaphore(2)


async def worker(name):
    async with semaphore:
        print(name, "start")
        await asyncio.sleep(2)
        print(name, "end")


await asyncio.gather(
    worker("A"),
    worker("B"),
    worker("C"),
    worker("D"),
)

# Сколько задач максимум одновременно находятся внутри async with semaphore? 2
# Через сколько примерно завершатся все четыре? 4 секунды
# Может ли C начать работу одновременно с A? нет
# Что произойдёт с C и D, пока A и B работают? они ждут async with semaphore: пока освободится место

# Для каждого сценария выбери:
# Lock
# Semaphore
# A = Lock
# B = Semaphore
# C = Lock
# D = Semaphore

event = asyncio.Event()


async def worker():
    print("worker waiting")

    await event.wait()

    print("worker started")


async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(2)

    print("setting event")
    event.set()

    await task


# Что произойдёт в первые 2 секунды? print("worker waiting")
# На чём остановится worker? await event.wait()
# Что делает event.set()? устанавливает событие
# Может ли worker продолжить выполнение после set()? да, он его и ждет
# Удаляет ли set() Event обратно в состояние unset? он устанавливает событие, не удаляет

event = asyncio.Event()

event.set()

print(event.is_set())

await event.wait()

print("passed")

event.clear()

print(event.is_set())

await event.wait()

print("never reached")

# Что выведется до clear()? True, passed
# Почему await event.wait() проходит сразу после set()? Потому что event произошел, он не сброшен
# Что изменяет clear()? сбрасывает event в unset
# На чём остановится последняя строка? await event.wait()

# Объясни, почему здесь Event, а не:
# - Lock
# - Semaphore
# - Queue
# Потому что это не ограничение на количество, а разрешение на выполнение кому нужно

# | Примитив  | Главная задача |
# | Lock      | Допустить только одну task конкурентно |
# | Semaphore | Допустить несколько task конкурентно |
# | Event     | Ожидание разрешения на выполнение |
# | Queue     | Синхронизированная асинхронная очередь |
# Чем Semaphore отличается от Queue? Семафор дает ограничение на количество, а queue создает очередь для выполнения
