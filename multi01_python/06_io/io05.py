file = open("test01.txt", "r", encoding="utf-8")

# read_txt = file.read()
# print(read_txt)


# readline_txt = file.readline()
# print(readline_txt)

readlines_txt = file.readlines()
print(readlines_txt)

file.close()