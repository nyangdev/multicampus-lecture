print (range(10))

for i in range(10):

    if(i % 2 == 0):
        continue
    else:
        print(i)

print("--------------------------------------------------")
print(list(range(10)))

list02 = list(range(10,20))
print(list02)

# 1에서 10까지 거꾸로
list03 = list(range(10,0,-1))
print(list03)

print("-----------------------과제---------------------------")
str = "hello, world!"
print(str[7:-1])
