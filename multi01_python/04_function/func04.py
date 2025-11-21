# def param02(a, b="default"):
#     print(a)
#     print(b)
#
# if __name__ == "__main__":
#     param02(1, 2)
#     param02("abc")
#     param02(a="def")
#     param02("aa", b="bb")

# data = [1,2,3]

# print(''.join(str(s) for s in data))

# hundred = [i for i in range(1,101)]
# print(hundred)
#
# five01 = [i for i in range(1,101) if not (lambda x: bool(x%5))(i)]
# print(five01)
#
# five02 = [i for i in range(1, 101) if (lambda x: x if (x%5) ==0 else None)(i)]
# print(five02)
#
# # zip
# print("----------------zip-----------------")
# num = [1, 2, 3]
# char = ["a", "b", "c"]
# zip_test = zip(num, char)
# print(zip_test)
# print(list(zip_test))
# print(dict(zip(num, char)))
#
# # map: 각각의 값에 함수를 실행
# print("----------------map-----------------")
# map_test = map(lambda  x : x*10, num)
# print(list(map_test))
#
# print(list(map(lambda x : x.upper(), char)))
#
# # filter
# print(filter(lambda x : x>1, num))
# print(list(filter(lambda x : x>1, num)))

# test_list에서 숫자만 새로운 list로 만들어서 출력
test_list = ["3", "6", None, "9", "", "a"]
# #list, filter,lambda 사용할것
remove_none = filter(None, test_list)
answer = filter(lambda x : x.isdigit() == True, remove_none)
answer_list = list(answer)
print(answer_list)

# 다른 방법
print(list(filter(lambda x : x.isdigit() if x else None, test_list)))