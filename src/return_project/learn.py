async def worker():
    print("worker start")
    await asyncio.sleep(3)
    print("worker done")
    return "result"


async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(1)

    try:
        await asyncio.shield(task)
    except asyncio.CancelledError:
        print("main cancelled")

# Что делает shield(task)? защищает от отмены task, если внешнюю task отменят
# Если main отменят во время await shield(task), что произойдёт с main? она print("main cancelled")
# Что произойдёт с task? продолжит выполнение
# Дойдёт ли worker до "worker done"? да

async def worker():
    try:
        print("start")
        await asyncio.sleep(5)
        print("done")
    except asyncio.CancelledError:
        print("worker cancelled")
        raise


async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(1)

    task.cancel()

    try:
        await asyncio.shield(task)
    except asyncio.CancelledError:
        print("main caught")

# task.cancel()
# → кто получает CancelledError?  и worker и main
# → shield спасает task или нет? нет, так как напрямую была task завершена

# await task и await asyncio.shield(task)
# Представь, что сама текущая задача была отменена.
# Что происходит в каждом варианте?
# Сформулируй принципиальную разницу.
# Если я правильно понял, что не сама task будет отменена а внешняя task которая ее вызывает, то
# await task и ее завершит, а shield спасет и продолжит выполнение

async def save_to_database():
    print("saving...")
    await asyncio.sleep(5)
    print("saved")


async def request_handler():
    task = asyncio.create_task(save_to_database())

    try:
        await asyncio.shield(task)
    except asyncio.CancelledError:
        print("client disconnected")

# клиент
#   ↓
# request_handler()
#   ↓
# save_to_database()

# Клиент отключился через 1 секунду.
# Почему здесь может быть полезен shield()? чтобы довести сохранение до конца, не отменилась task
# И почему не всегда стоит использовать shield() для таких операций? лишние ресурсы не использовать без необходимости
# дожидаться ответа если уже не нужно

async def worker():
    try:
        await asyncio.sleep(5)
        print("done")
    except asyncio.CancelledError:
        print("worker cancelled")
        raise


async def main():
    task = asyncio.create_task(worker())

    try:
        async with asyncio.timeout(1):
            await asyncio.shield(task)
    except TimeoutError:
        print("timeout")

    await asyncio.sleep(5)

# Через сколько будет TimeoutError? 1
# Будет ли worker отменён? нет
# Выведется ли done? да
# Зачем здесь shield() изменил поведение timeout()? чтобы в фоне продолжать выполнять task не дожидаясь его ответа

# Что именно защищает asyncio.shield() от cancellation, а что он НЕ защищает?
# от завершения внутреннего task из-за внешнего, не защищает от прямого завершения task