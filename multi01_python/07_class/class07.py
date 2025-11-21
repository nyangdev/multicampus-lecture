class HelloStaticDeco:

    class_val = "class variable"

    def __init__(self):
        self.name = "instance"

    # decorator
    # method를 함수처럼 사용하게 만든다
    @staticmethod
    def static_method():
        print(f"static method : {HelloStaticDeco.class_val}")

    def instance_method(self):
        print(f"instance method : {HelloStaticDeco.class_val}")
        print(self.name)

if __name__ == "__main__":
    class07 = HelloStaticDeco()
    class07.static_method()
    class07.instance_method()

    HelloStaticDeco.static_method()
    # HelloStaticDeco.instance_method()