msg = input("파일에 추가적으로 입력할 내용 : ")

file = open("test01.txt", "a", encoding="utf-8")

file.write(msg + "\n")

file.close()