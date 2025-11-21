from datetime import datetime
from time import sleep

def mylogger(name):
    def wrapper(func):
        def logging():
            print(f"{name} : {datetime.now()}")
            func()
            print(f"{name} : {datetime.now()}")

        return logging
    return wrapper

@mylogger("minji")
def greeting():
    sleep(2)
    print("hello, world!")

@mylogger("hong-gd")
def goodbye():
    sleep(2)
    print("bye, world")

if __name__ == "__main__":
    greeting()
    print("------------------")
    goodbye()

"""
데코레이터를 만들어두면 여러가지 다른 상황에서도 데코레이터를 이용해서 뭔가를 구현할수있음
"""