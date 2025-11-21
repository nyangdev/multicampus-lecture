class Parent:
    # class Parent(Object)와 같은 말임

    # 객체 생성(__init__가 호출)
    def __new__(cls, *args, **kwargs):
        print("parent new")
        print(args)

        # super() : 부모 객체
        return super().__new__(cls)

    # 변수 초기화
    def __init__(self):
        print("parent init")
        self.name = "parent"
        self.age = 100

    def prn01(self):
        print(f"prn01 : {self.name}")

    def prn02(self):
        print(f"prn02 : {self.name} / {self.age}")

# Parent를 상속받은 Child 클래스라고 선언하기
class Child(Parent):

    def __new__(cls, *args, **kwargs):
        print("child new")
        return super().__new__(cls, 10)

    def __init__(self):
        super().__init__()
        print("child init")
        self.name = "child"
        # self.age = 99
        # issue 부모클래스에서 가지고있는것들은 가져올수있음.
        # 부모의 객체에서 가지고있는것들은 자식이 가져올수없음.

if __name__ == "__main__":
    parent = Parent()
    parent.prn01()
    parent.prn02()

    print("----------------------")

    child = Child()
    child.prn01()
    child.prn02()