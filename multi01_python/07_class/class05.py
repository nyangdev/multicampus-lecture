class HelloGetterSetter:

    def __init__(self, name="홍길동"):
        self.name = name
        # 변수 앞에 __ : private -> class 내부에서만 사용 가능함
        self.__age = 100

    # @ -> decorator 기능 추가
    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.name}님은 {self.__age}세 입니다"

if __name__ == "__main__":
    class05 = HelloGetterSetter("김선달")
    print(class05)

    class05.age = 20
    print(class05)