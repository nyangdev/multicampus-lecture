from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int
    phone: str


@dataclass
class Address:
    addr: list[Person]

if __name__ == "__main__":
    hong = Person(name="홍길동", age=100, phone="010-1111-1111")
    lee = Person("이순신", 100, "010-2222-2222")
    kim = Person(name="김선달", age=100, phone="010-3333-3333")

    print(hong)
    print(lee)
    print(kim)

    print(f"{hong.name}님의 전화번호는 {hong.phone}입니다")

    print(hong > lee)

    addr = Address([hong, lee, kim])
    print(addr)