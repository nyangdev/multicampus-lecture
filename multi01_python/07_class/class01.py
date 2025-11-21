# 설계도
class HelloClass:

    def greetings(self):
        print("Hello, World!")

class TestClass:
    def hello(self):
        print("안농")

if __name__ == "__main__":
    # 변수 = 클래스() -> 객체화 = 메모리에 적재된다
    class01 = HelloClass()
    class01.greetings()

    print("-------------------------memory 주소--------------------------")
    # instance 저장되어있는 memory 주소
    print(class01)

    # isinstance()
    # class01이 HelloClass의 객체인지 아닌지를 판별해줌
    print(isinstance(class01, HelloClass))

    print("---------test-------------")
    class02 = TestClass()
    class02.hello()
    print(isinstance(class02, HelloClass))
    print(isinstance(class02, TestClass))


"""
특징 (4가지)
- 추상화 abstraction
- 상속 inheritance
- 다형성 polymorphism
- 캡슐화 encapsulation

원칙 (5가지)
- SRP (단일 책임 원칙)
- OCP (개방 폐쇄 원칙)
- LSP (리스코프 치환 원칙)
- ISP (인터페이스 분리 원칙)
- DIP (의존 역전 원칙)
"""