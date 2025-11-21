class Parent:
    def __init__(self):
        print("parent init")
        self.name = "parent"
        self.age = 100

    def prn01(self):
        print(f"prn01 : {self.name}")

    def prn02(self):
        print(f"prn02 : {self.name} / {self.age}")

class Child(Parent):

    def __init__(self):
        # 변수 초기화
        super().__init__()
        print("child init")
        self.name = "child"

if __name__ == "__main__":
    child = Child()
    child.prn01()
    child.prn02()