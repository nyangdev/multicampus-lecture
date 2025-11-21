answer_dictionary = dict()

name = input("이름 입력: ")
kor = input("국어: ")
math = input("수학: ")
eng = input("영어: ")

answer_dictionary["name"] = name
answer_dictionary["kor"] = int(kor)
answer_dictionary["math"] = int(math)
answer_dictionary["eng"] = int(eng)
answer_dictionary["sum"] = sum(value for key, value in answer_dictionary.items() if key != "name")
answer_dictionary["average"] = answer_dictionary["sum"]/3

print(answer_dictionary)