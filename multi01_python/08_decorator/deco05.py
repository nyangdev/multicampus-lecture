def greeting(func):

    def prn(*args, **kwargs):
        print("hello", end="")
        func(*args, **kwargs)

    return prn

@greeting
def myfunc01(name):
    print(name)

@greeting
def myfunc02():
    print("python!!!")

if __name__ == "__main__":
    myfunc01("minji")
    myfunc02()