def greeting(name):

    def wrapper(func):

        def prn():
            print(f"hello {name} !!")
            func()

        return prn

    return wrapper

@greeting("world")
def myfunc():
    print("hello, python !!")

if __name__ == "__main__":
    myfunc()
    # greeting("world!")(myfunc)()
    # == prn()