# Day 67: asyncio basics for my practice

import asyncio

async def my_hello():
    print("My hello start")
    await asyncio.sleep(0.1)
    print("My hello end")
    return "done"

asyncio.run(my_hello())

async def my_task(name, delay):
    print(f"My {name} starting")
    await asyncio.sleep(delay)
    print(f"My {name} finished")
    return f"{name} result"

async def my_main():
    my_results = await asyncio.gather(
        my_task("task-1", 0.1),
        my_task("task-2", 0.1),
        my_task("task-3", 0.1)
    )
    print(f"My results: {my_results}")

asyncio.run(my_main())

async def my_producer(queue):
    for i in range(5):
        await asyncio.sleep(0.05)
        await queue.put(f"My item {i}")
        print(f"My produced: item {i}")
    await queue.put(None)

async def my_consumer(queue):
    while True:
        my_item = await queue.get()
        if my_item is None:
            break
        print(f"My consumed: {my_item}")
        await asyncio.sleep(0.05)

async def my_queue_demo():
    my_q = asyncio.Queue()
    await asyncio.gather(
        my_producer(my_q),
        my_consumer(my_q)
    )

asyncio.run(my_queue_demo())

async def my_fetch(url):
    await asyncio.sleep(0.1)
    return f"My data from {url}"

async def my_fetch_all():
    my_urls = ["url1", "url2", "url3"]
    my_tasks = [my_fetch(url) for url in my_urls]
    my_results = await asyncio.gather(*my_tasks)
    print(f"My fetched: {my_results}")

asyncio.run(my_fetch_all())

async def my_timeout_demo():
    try:
        await asyncio.wait_for(asyncio.sleep(0.5), timeout=0.1)
    except asyncio.TimeoutError:
        print("My timeout occurred")

asyncio.run(my_timeout_demo())
