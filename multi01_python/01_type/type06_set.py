# set 순서x 중복x
a = {"1","3", "2", "4", "3"}
print(a)

# 숫자는 정렬(순서 존재)
b = {1,3,4,5,2,1}
print(b)
print([hash(x) for x in [1,2,3,4,5]])

# set()
c = set([1,2,3,4,5])
print(c)
print(type(c))
print(type([1,2,3,4,5]))

c.add(6)
print(c)
print(c.pop())
print(c)

# set() 안에 iterable한 객체 넣기
d = set("hello, world!")
print(d)

left = {'a', 'b', 'c', 'd'}
right = {'c', 'd', 'e', 'f'}

print(left.union(right))
print(left | right)

print(left.intersection(right))
print(left & right)

print(left.difference(right))
print(left - right)

# frozenset
e = frozenset({1,2,3,4,5})
print(e)

print(type(e))

print(dir(e))
print(dir(frozenset))
print(dir(set))