# 3)
def greeting(func):

    # 4)
    def prn(name):
        print("hello, ", end="")
        # 5)
        func(name)

    # 6)
    return prn
    # prn을 함수 실행한게 아니라 prn이라는 함수 자체를 값으로 리턴해주고 있는 형태임
    # 함수형 프로그래밍의 특징

# 2)
@greeting
def myfunc(name):
    print(name)

if __name__ == "__main__":
    # greeting(myfunc)("python!")
    # 1)
    # 7)
    myfunc("python!")