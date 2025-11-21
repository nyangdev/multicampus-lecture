def hello():
    while True:
        name = yield
        print(f"hello, {name}")

if __name__ == "__main__":
    coroutine = hello()
    # coroutine.__next__() 밑과 같은 뜻
    next(coroutine)

    # send() : yield를 통해 generator에 값을 전달
    coroutine.send("홍길동")
    coroutine.send("이순신")
    coroutine.send("김선달")