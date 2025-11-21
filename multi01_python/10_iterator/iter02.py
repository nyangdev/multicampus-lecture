my_iter = iter([1, 2, 3, 4, 5])

print(my_iter.__iter__())
print(my_iter)
print(type(my_iter))
# print(list(my_iter))

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# print(list(my_iter))

for i in my_iter:
    print(i, "test")