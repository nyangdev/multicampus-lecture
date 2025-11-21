def greeting(func):
    def prn():
        print("hello, ", end="")
        func()

    return prn

def myfunc():
    print("world")

if __name__ == "__main__":
    greeting(myfunc)()