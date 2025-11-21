class Hello:
    def __call__ (self, name):
        print(f"hello, {name}")

if __name__ == "__main__":
    greeting = Hello()
    # callable object : 객체를 함수처럼 사용
    greeting("배고프다그리고졸림헐")