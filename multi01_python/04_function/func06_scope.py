# 전역변수
x = 10
def test01():
    print("-------------test01-----------------")
    print(x)

test01()

def test02():
    # 지역변수
    x = 20
    print("-------------test02-----------------")
    print(x)


# test02()
# print("-------------전역-----------------")
# print(x)

def test03():
    # 전역변수 사용 want
    global x
    x = 30
    print("-------------test03-----------------")
    print(x)

test01()
test02()
test03()
test01()

print("--------------------------------------")

def test04():
    print("-------------test04-----------------")
    global y
    y = 3
    print(y)

test04()

print(y)

# shadowing 3개의 y는 모두 다른 y
def outer01():
    y = 6

    def inner01():
        y = 9
        print(f"inner y : {y}")

    inner01()
    print(f"outer y : {y}")

outer01()

print(f"global y : {y}")

print("--------------")


def outer02():
    print("--------------outer02-----------------")
    global y
    y = 6

    def inner02():
        y = 9
        print(f"inner : {y}")
    inner02()
    print(f"outer y : {y}")

outer02()
print(f"global y : {y}")

print("--------------")

def outer03():
    y = 9

    def inner03():
        nonlocal y
        y = 3
        print(f"inner y : {y}")

    inner03()
    print(f"outer y : {y}")

outer03()
print(f"global y : {y}")

# python namespace 찾아보기