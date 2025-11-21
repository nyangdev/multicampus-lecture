class HelloStr:
    def __init__(self, name="홍길동", age=100):
        self.name = name
        self.age = age

    # __str__ 원래 객체의 주소값을 리턴함
    # override 부모의 속성이나 기능을 재정의함 (*상속)
    def __str__(self):
        return f"name : {self.name} \t age : {self.age}"


if __name__ == "__main__":
    class04 = HelloStr(name="이순신", age=10)
    print(class04)