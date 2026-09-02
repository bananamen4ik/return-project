queue = asyncio.Queue()

await queue.put("A")
await queue.put("B")
await queue.put("C")

print(queue.qsize())

print(await queue.get())
print(await queue.get())

print(queue.qsize())

# Что выведет первый qsize()? 3
# Что выведут два get()? A, B
# Что выведет второй qsize()? 1
# В каком порядке будут получены элементы? A, B, C. FIFO

async def consumer(queue):
    print("waiting")

    item = await queue.get()

    print("got:", item)


async def producer(queue):
    await asyncio.sleep(2)
    await queue.put("hello")
    print("put")


async def main():
    queue = asyncio.Queue()

    consumer_task = asyncio.create_task(consumer(queue))
    producer_task = asyncio.create_task(producer(queue))

    await asyncio.gather(
        consumer_task,
        producer_task,
    )

# Что напечатается первым? print("waiting")
# Через сколько примерно появится "got: hello"? 2 секунды
# Что делает consumer всё это время? ожидает появление в очереди элемента
# Выполняется ли consumer или она блокирует весь event loop? выполняется насколько логично я понимаю

queue = asyncio.Queue(maxsize=2)

await queue.put("A")
await queue.put("B")

print("before")

await queue.put("C")

print("after")

# Дойдёт ли выполнение до "after"? нет
# Почему? так как максимальный размер 2
# Что должно произойти с очередью, чтобы put("C") продолжился? пока не освободится место в очереди будет блокировка

async def worker(queue):
    while True:
        item = await queue.get()

        print("processing", item)

        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    worker_task = asyncio.create_task(worker(queue))

    for i in range(3):
        await queue.put(i)

    await asyncio.sleep(4)

# Сколько элементов обработает worker? 3
# В каком порядке? 0, 1, 2
# Почему worker не забирает все три элемента одновременно? каждый .get вызывается с задержкой sleep
# Что происходит с worker после обработки 2? продолжает дальше ждать .get как обычно

async def worker(queue):
    item = await queue.get()

    print("processing", item)

    await asyncio.sleep(2)

    queue.task_done()


async def main():
    queue = asyncio.Queue()

    await queue.put("A")

    asyncio.create_task(worker(queue))

    print("before join")

    await queue.join()

    print("after join")

# Что выведется первым? print("before join")
# Через сколько примерно "after join"? 2 секунды
# Почему join() знает, что worker закончил? worker вызвал queue.task_done() и была одна task теперь 0
# Что произойдёт, если убрать queue.task_done()? join не узнает и продолжит ждать

async def worker(queue):
    while True:
        item = await queue.get()

        try:
            print("processing", item)
            await asyncio.sleep(1)
        finally:
            queue.task_done()

# Почему task_done() здесь лучше помещать в finally? чтобы в любом случае вызвался task_done и счетчик был надежным
# даже в случаях исключений любых

async def worker(name, queue):
    while True:
        item = await queue.get()

        try:
            print(name, "processing", item)
            await asyncio.sleep(1)
        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker("W1", queue)),
        asyncio.create_task(worker("W2", queue)),
        asyncio.create_task(worker("W3", queue)),
    ]

    for i in range(6):
        await queue.put(i)

    await queue.join()

    for worker_task in workers:
        worker_task.cancel()

    await asyncio.gather(*workers, return_exceptions=True)

# Сколько workers одновременно обрабатывают задачи? 3
# Сколько элементов одновременно может обрабатываться? 3
# В каком порядке элементы забираются из Queue? 0, 1, 2, 3, 4, 5
# Что делает queue.join()? ждет пока queue обнулиться счетчик выполняющихся
# Зачем после join() вызывается cancel()?  чтобы завершить task workers, и они дальше не ждали .get queue
# Почему workers не завершаются сами после обработки шести элементов? из-за while true и await queue.get()
# Зачем здесь return_exceptions=True? Чтобы наружу не выводились исключения Cancelled

# Чем Queue принципиально отличается от gather()? Можно регулировать нагрузку на систему сколько конкурентных
# задач будет выполняться