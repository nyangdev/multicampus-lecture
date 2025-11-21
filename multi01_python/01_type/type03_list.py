# list tuple set dictionary
# sequence : 순서가 있는 값들을 가진 객체

# list : 순서 o, 중복 o
print("------------list------------")
a = [55,3,2,41,87,99]
print(a)
print(type(a))

print("------------sort test------------")
a.sort()
print(a)

print("------------reverse test------------")
a.reverse()
print(a)

a.append(6)
print(a)

b = list()
print(type(b))
print("------------before append------------")
print(b)

print("------------after append------------")
b.append(6)
b.append(7)
b.append(8)
b.append(9)
print(b)

print("------------index test------------")
print("list a 프린트하기")
print(a)
print("특정 index 조회하기")
print(a[2])
print("list b 프린트하기")
print(b)
print("특정 index 조회하기")
print(b[0])

# dir : 객체의 속성, 메서드 확인
print("------------dir 연습------------")
print(dir(b))
print(dir(a))
print(dir(a[0]))
print(dir(3))

print("------------pop test------------")
print(a)
print(a.pop())
print(a)

print(a.pop(1))
print(a)

print("------------len test------------")
print(len(a))

print("list a")
print(a)
print("list b")
print(b)

print("list c")
c = a+b
print(c)

print(type(c))

print(a*2)

print(c)
c.insert(3,999)
print(c)

# 중첩
d = ['a','b','c','d','e', ['f','g','h'], 'i']
print(d)
print(len(d))
print(d[5])
print(d[5][0])

# g print
print(d[5][1])