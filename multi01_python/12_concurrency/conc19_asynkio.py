import asyncio

# coroutine
# 함수 앞에 async
async def hello(name):
    print(f"hello, {name}")
    # 비동기적으로 실행하고싶은 객체 앞에 await
    await asyncio.sleep(3)
    print("nice to meet you")


if __name__ == "__main__":
    # 동기적으로 실행
    asyncio.run(hello("async"))
    asyncio.run(hello("coroutine"))