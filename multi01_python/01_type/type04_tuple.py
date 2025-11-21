# tuple은 변경 불가능한 리스트 (불변)

print("----------------tuple a---------------")
a = (1,2,3)
print(a)
print(type(a))

print("----------------tuple d---------------")
b = tuple([5,6,7,8])
print(b)
print(type(b))

print(b.count(5))

c = a + b
print(c)
print(type(c))

print("----------------형변환---------------")
d = list(c)
print(d)
print(type(d))

d.remove(7)
print(d)

f = tuple(d)
print(type(f))

print("----------------packing---------------")
# packing
g = 1,2,3
print(g)
print(type(g))

print("----------------unpacking---------------")
h, i, l = g
print(h)
print(i)
print(l)
print(type(g))
print(g)