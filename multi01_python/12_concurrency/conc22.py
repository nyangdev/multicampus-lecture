import asyncio

async def hello(future, name):
    print(f"hello, {name}")
    await asyncio.sleep(3)
    future.set_result("nice to meet you")

async def main():
    loop = asyncio.get_event_loop()

    future01 = loop.create_future()
    future02 = loop.create_future()

    loop.create_task(hello(future01, "a"))
    loop.create_task(hello(future02, "2"))

    print(await future01)
    print(await future02)

if __name__ == "__main__":
    asyncio.run(main())