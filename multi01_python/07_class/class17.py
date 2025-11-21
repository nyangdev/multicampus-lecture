from abc import ABCMeta, abstractmethod

class Character(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Knight(Character):
    def attack(self):
        print(f"{self.name} : 칼로 공격!")

class Archer(Character):
    def attack(self):
        print(f"{self.name} : 활로 공격!")

if __name__ == "__main__":
    character = None

    select = int(input("1:기사 2:궁수 \n 직업을 선택해주세요 : "))

    match select:
        case 1:
            character = Knight("기사")

        case 2:
            character = Archer("궁수")

    character.attack()

    # polymorphism : 다형성