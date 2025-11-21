def exception01():
    print(10 / 0)

def exception02():
    try:
        print(10 / 0)
    except :
        print("0으로 나눌 수 없습니다")


def exception03():
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")

def exception04():
    try:
        a = [1,2,3,4,5]
        print(a[5])
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")

def exception05():
    try:
        a = [1,2,3,4,5]
        print(a[5])
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
    except IndexError:
        print("인덱스를 다시 확인해주세요.")


def exception06():
    try:
        a = [1,2,3,4,5]
        print(a[5])
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)

def exception07():
    try:
        a = [1,2,3,4,5]
        print(a[5])
    except Exception as e:
        print(e)

def exception08():
    try:
        a = [1,2,3,4,5]
        print(a[5])
    except Exception as e:
        print("예외 발생")
    else:
        print("예외 발생 안함")
    finally:
        print("무조건 실행")


def exception09():
    try:
        a = [1,2,3,4,5]
        print(a[4])
    except Exception as e:
        print("예외 발생")
    else:
        print("예외 발생 안함")
    finally:
        print("무조건 실행")

if __name__ == "__main__":
    # exception01()
    # exception02()
    # exception03()
    # exception04()
    # exception05()
    # exception06()
    # exception07()
    # exception08()
    exception09()