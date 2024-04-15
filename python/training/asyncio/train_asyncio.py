import asyncio
import time
from asyncio import Task


async def say_after(delay, what) -> None:
    await asyncio.sleep(delay=delay)
    print(what)


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    await say_after(delay=1, what="hello")
    await say_after(delay=2, what="world")

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main())


# create_task()
async def main_2() -> None:
    task1: Task[None] = asyncio.create_task(coro=say_after(delay=1, what="hello"))
    task2: Task[None] = asyncio.create_task(coro=say_after(delay=2, what="world"))

    print(f"Started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")


# asyncio.run(main_2())


# TaskGroup.create_task()
async def main_3() -> None:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro=say_after(delay=1, what="hello"))
        tg.create_task(coro=say_after(delay=2, what="world"))
        print(f"Started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.
    print(f"Finished at {time.strftime('%X')}")


asyncio.run(main=main_3())
