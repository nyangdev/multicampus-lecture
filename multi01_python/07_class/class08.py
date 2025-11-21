class HelloClassDeco:

    # class 변수 : 해당 class로 만드러진 instance 전체가 공유
    cnt = 0

    def __init__(self):
        self.name = "class decorator"
        HelloClassDeco.cnt += 1

    # classmethod decorator : class를 받는다
    # staticmethod와 다른 점은 상속일때 확인 가능
    @classmethod
    def class_method(cls):
        # cls는 class 별칭
        print(cls.cnt)

    # 객체가 메모리에서 반환될때 호출된다
    # garbage collected
    def __del__(self):
        HelloClassDeco.cnt -= 1

if __name__ == "__main__":
    # 클래스 이름뒤에 괄호 사용
    class08_1 = HelloClassDeco()
    class08_2 = HelloClassDeco()
    class08_3 = HelloClassDeco()

    print(class08_1.cnt)
    class08_2.class_method()
    HelloClassDeco.class_method()

    del class08_3
    # print(class08_3)

    print(class08_1.cnt)