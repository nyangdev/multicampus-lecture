class Greeting:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            print(f"hello {self.name}")
            func(*args, **kwargs)

        return wrapper

@Greeting("python")
def myfunc():
    print("hello world")

if __name__ == "__main__":
    myfunc()
    # Greeting("python")(myfunc)()