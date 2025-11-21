class singleton(type):
    # instance 주소 저장
    __instance = {}

    # __call__ : class를 함수처럼 호출할 수 있도록 만든다
    # -> callable object
    def __call__(self, *args, **kwargs):
        if self not in self.__instance:
            self.__instance[self] = super().__call__(*args, **kwargs)
        return self.__instance[self]

class MyClass(metaclass=singleton):
    pass

if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    print(a)
    print(b)

    print(a == b)