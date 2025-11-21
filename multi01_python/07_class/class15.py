from abc import ABC, abstractmethod

# ABC : Abstract Base Class
# ABC를 상속받음
class AbstractParent(ABC):
    def prn(self):
        print("abstract class : abstract method를 가질 수 있는 class")

    @abstractmethod
    def abstract_method(self):
        pass

class Child(AbstractParent):
    def abstract_method(self):
        print("abstract method : 상속받은 자식 클래스에서 반드시 구현")

if __name__ == "__main__":
    # abstract_parent = AbstractParent
    # 추상 클래스 (AbstractParent)는 객체 생성 불가

    child = Child()
    child.prn()
    child.abstract_method()