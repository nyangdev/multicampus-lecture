import asyncio


async def hello(name):
    print(f"hello, {name}")
    await asyncio.sleep(3)
    print("nice to meet you")


async def main():
    await hello("coroutine")

    hello01 = asyncio.create_task(hello("async"))
    hello02 = asyncio.create_task(hello("coroutine"))

    await hello01
    await hello02
    print(hello01)
    print(dir(hello01))


if __name__ == "__main__":
    # 비동기적 실행
    # 고수준 실행
    # asyncio.run(main())

    # 저수준 실행
    # 더 많은 기능을 사용할 수 있다
    # new_event_loop() : event loop를 생성
    # event loop : 전체적인 조율 / 처리
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()