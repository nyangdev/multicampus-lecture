# import math
import math as m

def circle(r):
    return m.pi * r * r

if __name__ == "__main__":
    r = input("반지름 입력")
    print(f"반지름이 {r}인 원의 넓이는 {circle(int(r))} 입니다.")
