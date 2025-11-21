'''
*
**
***
****
*****
'''
def star01():
    print("----------------------------star01----------------------------")
    # for i in range(1,6):
    #     print("*"*i)
    for i in range(5):
        for j in range(i+1):
            print("*", end = "")
        print()



'''
*****
****
***
**
*
'''
def star02():
    print("----------------------------star02----------------------------")
    # for i in range(5,0, -1):
    #     print("*"*i)
    for i in range(5):
        print("*" * (5-i))



'''
    *
   **
  ***
 ****
*****
'''
# 1 2 3 4 5
# 5 4 3 2 1
def star03():
    print("----------------------------star03----------------------------")
    # for i in range(1, 6):
    #     print(" " * (5-i) + "*" * i)
    for i in range(5):
        print(" " * (4-i) + "*" * (i+1))



'''
*****
 ****
  ***
   **
    *
'''
def star04():
    print("-----------------------------star04-----------------------------")
    # for i in range(5, 0, -1):
    #     print(" "* (5-i) + "*" * i)
    for i in range(5):
        print(" " * i + "*" * (5 - i))



'''
    *
   ***
  *****
 *******
*********
'''
def star05():
    print("-----------------------------star05----------------------------")
    # for i in range(1, 6):
    #     print("i" * (5-i) + "*" * i + "*" * (i-1))
    #     print(" " * (5 - i) + "*" * i + "*" * (i - 1))
    for i in range(5):
        print(" " * (4-i) + "*" * (2 * i + 1))


if __name__ == '__main__':
    star01()
    star02()
    star03()
    star04()
    star05()
