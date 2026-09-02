import asyncio
import time


def sync_worker(name):
    print(name, "start")
    time.sleep(2)
    print(name, "end")


async def main():
    await asyncio.gather(
        sync_worker("A"),
        sync_worker("B"),
    )


asyncio.run(main())


# Что произойдёт и сколько примерно будет выполняться?
# Просто поочередно вызовется sync_worker("A"), sync_worker("B") и упадет программа: gather ожидает корутину
# 4 секунды

# 2
async def main():
    await asyncio.gather(
        asyncio.to_thread(sync_worker, "A"),
        asyncio.to_thread(sync_worker, "B"),
    )

asyncio.run(main())

# 3
# Разница между await asyncio.sleep(2) и await asyncio.to_thread(sync_worker)
# await asyncio.sleep(2) выполняется напрямую в том же event loop, а sync_worker будет выполняться в отдельном потоке

# 4
async def main():
    task = asyncio.create_task(
        asyncio.to_thread(sync_worker, "A")
    )

    await asyncio.sleep(0.1)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("cancelled")

# Получит ли sync_worker() CancelledError? Нет
# Остановится ли time.sleep(2)? Нет
# Что произойдёт с самим async task? Прервет ожидание sync_worker, но без взаимодействия на него
# Может ли "A end" появиться после "cancelled"? Да