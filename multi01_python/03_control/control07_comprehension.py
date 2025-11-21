list01 = list()
for i in range(1, 11):
    list01.append(f"a{i}")

print(list01)

list02 = [f"a{i}" for i in range(1, 11)]
print(list02)

# 1에서 10 사이 짝수만 list로
list03 = [i for i in range(1, 11) if i%2 == 0]
print(list03)

subjects = [
    "python", "analysis", "database",
    "html", "css", "javascript", "django",
    "science", "engineering"
]

list04 = [f"{i}" for i in subjects if "a" in i]
print(list04)