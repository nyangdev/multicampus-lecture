class Greeting:

    def __init__(self, func):
        self.func = func

    # callable object : 객체를 함수처럼 호출
    # 인스턴스 뒤에 괄호를 붙일수있는데 __call__ 함수덕분임
    def __call__(self, *args, **kwargs):
        print("hello", end=" ")
        self.func(*args, **kwargs)

# @Greeting
def myfunc():
    print("world!")

if __name__ == "__main__":
    # myfunc()
    Greeting(myfunc)()