a = 100
print(a)

b = int(101)
print(b)

c = 200.2
print(c)

d = float(200.3)
print(d)

print(a + d)

print(type(a + d))

z = a+d

print(type(z))

print("-------complex test-------")
# complex 복소수
# real + imaginary (실수부+허수부j)
e = 1 + 2j
print(e)
print(type(e))

f = complex(3, 4)
print(f)


print("-------boonlean test-------")

g = True
h = False

print(type(g))
print(type(h))

print("-------type check-------")
print(type(g))

# 1 true 0 false
print("-------number t/f test-------")
print(1 == g)
print(0 == g)

print("-------2/8/16진수 test-------")
# 2진수 0b
binary = 0b1111
print(binary)

# 8진수
octal = 0o77
print(octal)

# 16진수
hexadecimal = 0xff
print(hexadecimal)