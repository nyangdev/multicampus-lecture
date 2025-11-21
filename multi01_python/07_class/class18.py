class A:
    pass

class CreateMeta(type):
    def __new__(cls, *args, **kwargs):
        print("metaclass new")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("metaclass init")

    # callable object로 만들어준다
    def __call__(self, *args, **kwargs):
        print("metaclass call")
        return super.__call__()

if __name__ == "__main__":
    num = 10
    print(type(num))

    print(type(A))
    # A라는 class
    # 값의 형태가 type
    # = "A라는 class" 라는 인스턴스의 타입이 type

    # type을 이용하여 class 생성
    # type = class를 생성하는 class = metaclass
    hello_type = type("HelloWorld", (), {})
    # hello_type은 HelloWorld라는 class

    print(hello_type)
    # hello_type을 instance화 하니까 객체가 만들어짐
    # hello_type은 클래스

    hello = hello_type()
    print(hello)

    print("-----------")

    metaclass = CreateMeta("MyClass", (), {})
    print(metaclass)

    instance = metaclass()
    print(instance)