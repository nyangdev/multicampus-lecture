class HelloFields:
    def __init__(self, name = "홍길동", age = 100):
        # 속성 fields
        self.name = name
        self.age = age

    # 명명규칙
    # camel case : 소문자. 새로운 단어가 나타나면 대문자로 시작
    # pascal case : 첫글자도 대문자. 새로운 단어가 나타나면 대문자로 시작
    # snake case : 소문자. 새로운 단어가 나타나면 _ 로 이어줌
    # kebab case : 소문자. 새로운 단어가 나오면 - 으로 이어줌
    # python은 변수, 함수(method), module 은 camel case
    # class는 pascal case
    # 상수를 표현할때는 모든 문자를 대문자, snake_case 따름
    def members_info(self):
        return(f"이름 : {self.name} \t 나이 : {self.age}")

if __name__ == "__main__":
    class03 = HelloFields()
    print(class03.members_info())

    dongheon = HelloFields("dongheon", 100)

    print(dongheon.members_info())

    # 변수
    # ■ 인스턴스 변수 추가 ■
    dongheon.addr = "수원시"

    print(f"{dongheon.members_info()} \t 지역 : {dongheon.addr}")

    # ■ 다른 객체에서 사용 불가함 ■
    # print(f"{class03.members_info()} \t 지역 : {class03.addr}")