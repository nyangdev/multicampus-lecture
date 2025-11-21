from abc import ABCMeta, abstractmethod

# metaclass : class를 만들어주는 class
class AbstractParent(metaclass=ABCMeta):
    def prn(self):
        print("추상 클래스")

    @abstractmethod
    def abstractmethod(self):
        pass

class Child(AbstractParent):
    def abstractmethod(self):
        print("추상 메서드")

if __name__ == "__main__":
    child = Child()
    child.prn()
    child.abstractmethod()