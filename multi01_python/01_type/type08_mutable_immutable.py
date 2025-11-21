# mutable : list, set, dictionary 가변
a = [1, 2, 3, 4, 5]
print(a)
print(id(a))

a.append(6)
print(a)
print(id(a))

# immutable : numbers, tuple, str, frozenset 불변
b = 10
print(b)
print(id(b))

b = 20
print(b)
print(id(b))

c = (1,2,3,4,5)
print(c)
print(id(c))

c = c + tuple(a)
print(c)
print(id(c))