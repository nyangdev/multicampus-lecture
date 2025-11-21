class Person:
    def prn(self):
        print("person")

class Father(Person):
    def prn(self):
        print("father")


class Mother(Person):
    def prn(self):
        print("mother")

class Child(Father, Mother):
    pass

if __name__ == "__main__":

    child = Child()
    child.prn()

# 파이썬의 다이아몬드 상속 대처# 다른 언어에서의 다이아몬드 상속은????? (자바에서 어떻게 하는지 찾아보기)


# 메서드 탐색 순서 (MRO : Method Resolution Order) 에서 가까운 순서대로 찾아옴
    print(Child.mro())