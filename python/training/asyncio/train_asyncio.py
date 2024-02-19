import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main())


# create_task()
async def main_2():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"Started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")


# asyncio.run(main_2())


# TaskGroup.create_task()
async def main_3():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "hello"))
        tg.create_task(say_after(2, "world"))
        print(f"Started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.
    print(f"Finished at {time.strftime('%X')}")


asyncio.run(main_3())
