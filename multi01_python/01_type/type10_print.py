#flush : stream에 남아있는 데이터를 강제로 출력

name = "minji"
age = 25

print(name)
print(age)
print("name " + name)

print(name, age)
print(name, age, sep='     ')
print(name, age, sep='-')

print(name, age, end='끝남끝끝')
print("안농")

print("name", name, sep=":", end="\t")
print("age", age, sep=":")

# % values
print("name : %s" %name)
print("age : %d" %age)

print("name: %s \t age: %d" %(name, age))

# str.format()
print("name: {} \t age: {}".format(name, age))

#f-string
print(f"name: {name} \t age: {age}")