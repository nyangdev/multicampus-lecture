a = 'hello, world'
print(a)
print(type(a))

# escape sequence
b = 'hello, "python"'
print(b)

b = "hello, 'python'"
print(b)

b = 'hello, \'python\''
print(b)

c = '''hello
this
world
   weird'''

print(c)

e = "hello, world"
print(e)

f = """hello
world
        idk
                                    that"""
print(f)

g = "hello, 'python'"
h = 'hello, "python"'
print(g)
print(h)

# str()
i = str("hello, world")
print(i)

# escape sequence
print("hello, \nworld")

# raw string
j = "c:\test"
print(j)

j = r"c:\test"
print(j)

print("hello" + " " + "world" + "!!")

# - 는 동작 x
print("hello"*2)

print("hello" + str(2))