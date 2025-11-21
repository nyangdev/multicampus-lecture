def greeting(func):
    def prn():
        print("hello, ", end="")
        func()

    return prn

# decorator로 만들면 greeting이라는 함수에 myfunc가 값으로 전달되는 형태다
@greeting
def myfunc():
    print("world")

if __name__ == "__main__":
    # greeting(myfunc)()
    myfunc()