# match ~ case

a = input("1 ~ 3 사이의 정수값을 입력해주세요 : ")

match a :
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")

    case _ :
        print("default")