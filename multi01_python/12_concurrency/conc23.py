import asyncio

async def mysum():
    print("start")
    result = 0
    for i in range(1, 101):
        result += i
    await asyncio.sleep(3)
    print("end")
    return result

async def main():
    result = await asyncio.gather(mysum(), mysum(), mysum())
    return result

if __name__ == "__main__":
    print(asyncio.run(main()))