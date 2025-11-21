# iterable 반복 가능한 (순서대로 값을 꺼내올 수 있는)
# iterator 반복 가능한 객체 (순서대로 값을 꺼내올 수 있는 객체)
# lazy evaluation 실행될때 연산된다
# __iter__() : iterator 반환

nums = list(range(1, 11))
print(nums)
print(dir(nums))


nums_iter = nums.__iter__()
print(nums_iter)
print(type(nums_iter))

# for i in range(1, 11):
#     if i == 11:
#         break
#     print(nums_iter.__next__())

print(nums_iter.__next__())
print(nums_iter.__next__())
print(nums_iter.__next__())

print(list(nums_iter))

print(list(nums_iter))
# print(nums_iter.__next__())

nums_iter2 = nums.__iter__()
# print(list(nums_iter2))
for item in nums_iter2:
    print(item)