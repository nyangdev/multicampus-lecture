# fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34

# 앞에 두 개 보고 더해서 출력하는 애
def fibo(n):
    # if n <=1:
    #     return n
    # else:
    #     return fibo(n-1) + fibo(n-2)
    a, b = 0, 1
    i = 0 #카운트용 변수
    while i < n:
        print(a, end = " ")
        a, b = b, a+b
        i += 1


if __name__ == '__main__':
    n = int(input('출력할 갯수 입력 : '))

    # for i in range(n):
    #     print(fibo(i), end=" ")
    fibo(n)