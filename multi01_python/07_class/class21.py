# special method (magic method)

"""
__ge__() : >=
__gt__() : >
__le__() : <=
__lt__() : <
__eq__() : ==
__ne__() : !=


__add__() : +
__sub__() : -
...

__str__() : 객체 표현 값 리턴 (사람을 위한)
__repr__() : 객체 표현 값 리턴 (다른 객체를 위한)
# print()는 __str__ 먼저 호출, 없으면 __repr__ 호출
# __repr__로 리턴되는 값은 eval() 의 arg로 값을 넣었을때,
# 객체가 생성되는 표현 값을 리턴하도록 권장
"""

class Line:

    def __init__(self, length=0):
        self.length = length
        print(f"길이 {length}를 가지는 선이 생성되었습니다.")

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self, other):
        return self.length != other.length

    def __str__(self):
        return f"{self.length}의 길이를 가진 선"

    def __repr__(self):
        return f"Line(length={self.length})"

if __name__ == "__main__":
    line10 = Line(10)
    line3 = Line(3)

    print(f"line10 : {line10.length}")
    print(f"line10 : {line3.length}")

    print(f"line10 + line3 : {line10 + line3}")
    print(f"line10 - line3 : {line10 - line3}")

    print(f"line10 > line3 : {line10 > line3}")
    print(f"line10 >= line3 : {line10 >= line3}")
    print(f"line10 < line3 : {line10 < line3}")
    print(f"line10  line3 : {line10 <= line3}")

    print(f"line10 == line3 = {line10 == line3}")
    print(f"line10 != line3 = {line10 != line3}")

    print(line10)
    print(F"__str__ : {line10.__str__()}")
    print(f"__repr__ : {line10.__repr__()}")

    # eval : 실행
    eval(f"{line10.__repr__()}")
    eval("print(Line(3) + Line(4))")