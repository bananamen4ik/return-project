import asyncio


async def worker():
    print("start")

    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("cancelled")
        raise

    print("end")


async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(1)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("main caught cancellation")

# Полный вывод:
# print("start"), print("cancelled"), print("main caught cancellation")

# Выведется ли end? нет
# Выведется ли cancelled? да
# Выведется ли main caught cancellation? да
# Что будет с task.cancelled() после await task? Если сразу написать следующей строчкой, то он не выполнится так как except сработает
# Но если после except например написать, то будет True

async def worker():
    try:
        await asyncio.sleep(5)
    finally:
        print("finally")

task = asyncio.create_task(worker())

await asyncio.sleep(1)

task.cancel()

try:
    await task
except asyncio.CancelledError:
    print("cancelled")

# порядок вывода: print("finally"), print("cancelled")
# Выполнится ли finally, несмотря на отмену? Да, finally при любых обстоятельствах выполняется

async def main():
    try:
        async with asyncio.timeout(2):
            await asyncio.sleep(5)
            print("done")
    except TimeoutError:
        print("timeout")

# через сколько примерно секунд? 2
# что будет выведено? print("timeout")
# будет ли "done"? нет

async with asyncio.timeout(2):
    await asyncio.sleep(5)

# A. TimeoutError
# B. asyncio.sleep(5)
# C. CancelledError
# D. истекли 2 секунды
# E. timeout() преобразует CancelledError

# Порядок: B, D, C, E, A

async def worker():
    await asyncio.sleep(5)
    return "done"

# A
task = asyncio.create_task(worker())

done, pending = await asyncio.wait(
    {task},
    timeout=1,
)

# B
try:
    async with asyncio.timeout(1):
        await worker()
except TimeoutError:
    print("timeout")

# A:
# через сколько вернётся? 1
# task продолжит работу? да
# pending = set(task)
#
# B:
# через сколько будет TimeoutError? 1
# worker продолжит работу? нет

# 6
async def worker():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("cancelled")

task = asyncio.create_task(worker())

await asyncio.sleep(1)

task.cancel()

await task

print(task.cancelled())

# Будет напечатано: print("cancelled"), последний print не будет напечатан, так как нет except CancelledError

# 7
async def worker():
    await asyncio.sleep(5)
    return "done"

try:
    result = await asyncio.wait_for(
        worker(),
        timeout=1,
    )
except TimeoutError:
    print("timeout")

# 1. Через сколько примерно будет TimeoutError? 1
# 2. Что произойдёт с worker()? отменится
# 3. Чем этот пример концептуально отличается от wait(timeout=1)? тем что таск отменяется

# task.cancel() - отменить задачу
# asyncio.timeout() и asyncio.wait_for() - через заданное время отменить задачу
# asyncio.wait(..., timeout=...) - через заданное время вернуть done, pending и не отменять задачу

# В чём принципиальная разница между «перестать ждать операцию» и «отменить операцию»?
# Разница в том, что мы возвращаем текущее состояние всех задач, но не отменяем их
