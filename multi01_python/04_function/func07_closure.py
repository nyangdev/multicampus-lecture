def greetings(name):
    prefix = "안녕하세요! "

    # lexical scope : suffix라는 함수가 선언될때 함수의 범위가 정해진다
    # suffix가 return 되면 greetings도 종료되지만 suffix를 실행 시 greetings의 환경(prefix,name)를 기억했다가 사용
    def suffix():
        return prefix + name + "님!! 환영합니다!!"

    # 함수가 값으로 사용됨 - 일급객체, 일급함수
    return suffix

if __name__ == "__main__":
    message = greetings("김민지")()
    print(message)