class MyException(Exception):

    def __init__(self):
        super().__init__("내가 만든 예외")

def user_define_exception():
    try:
        a = 1
        b = 2
        if a + b == 3:
            raise MyException()
            # raise : 예외를 강제로 발생시키는 키워드
    except MyException as e:
        print(e)

if __name__ == "__main__":
    user_define_exception()