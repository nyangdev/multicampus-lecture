# 1
'''
*********
 *******
  *****
   ***
    *
'''


def star01():
    for i in range(5):
        print(" " * i + "*" * (9-i*2))


if __name__ == "__main__":
    star01()