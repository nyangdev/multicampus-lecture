class HelloSelf:

    # 속성
    # class variable : 해당 클래스를 통해 만들어진 모든 객체가 사용 가능함
    suffix = "님, 반갑습니다!"

    # 앞뒤로 __ 붙은 method : special method || magic method
    # __init__(self) : __new__() 호출하여 객체를 생성합니다 / instance 변수를 초기화 시켜줌
    def __init__(self):
        # 속성
        # 인스턴스 변수 instance variable : 객체 각각이 다른 값을 가질수있음
        self.prefix = "안녕하세요, "

    # 기능
    # function (기능) 독립적
    # method (기능) 종속적
    # greetings 는 HelloSelf 라는 클래스 안에 들어가 있음. method로 봄
    # self : 나 자신 객체를 말함 instance
    def greetings(self, name):
        print(f"{self.prefix} {name} {HelloSelf.suffix}")

if __name__ == "__main__":
    class02 = HelloSelf()
    class02.greetings("배고팡 아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ진짜배고파저녁먹고잘걸")

    # greetings는 self (나 자신, instance) 가 필요하다
    # 객체로 만들어져야 사용 가능하다
    # HelloSelf.greetings("배고프다거ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ")\

    print(HelloSelf.suffix)


    # print(HelloSelf.prefix)
    print(class02.prefix)
    print(class02.suffix)