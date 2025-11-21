# dictionary
# 순서 있음, 중복(key 비허용, value 허용)
dict01 = {"야":1, "집가고싶당":2}
print(dict01)
print(type(dict01))
print(dict01["야"])
print(dict01["집가고싶당"])

dict01['c'] = 3
print(dict01)

dict01["진짜집가고싶닼"] = 222222222222
print(dict01)

# dict()
dict02 = dict(a=1, b=3, 냐냐냐 = 3)
print(dict02)

dict03 = dict([['a',1], ['b', 2]])
print(dict03)

print(dict03.keys())
print(dict02.keys())

ddd = dict03.keys()
print(type(ddd))

print("-----keys,values,items 빼내기-----")
print(dict03.keys())
print(dict03.values())
print(dict03.items())
print("-----종료-----")


dict04 = dict([ ('a',1), ('b',2) ])
print(dict04)
print(type(dict04))

print(dict04.keys())

print(type(dict04.keys()))

print("-----keys,values,items 빼내기-----")
print(dict03.keys())
print(dict03.values())
print(dict03.items())
print("-----종료-----")

print("---- tuple list 변경처리 ----")
aaa = dict03.keys()
print(aaa)
print(type(aaa))
bbb = list(dict03.keys())
print(bbb)
print(type(bbb))

# aaa는 튜플이라서 append 불가
# aaa.append(1)
bbb.append(1)
print(bbb)