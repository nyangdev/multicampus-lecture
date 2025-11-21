# 3! = 3*2*1

def factorial_loop(n):
    fac = 1
    for i in range(n, 0, -1):
        fac *= i

    return fac

def factorial_recursion(n):
    # 종료 조건 반드시 작성
    if n == 1:
        return 1

    return n * factorial_recursion(n - 1)
    # 5! = 5 * factorial_recursion(4)
    #   = 5 * 4 * factorial_recursion(3)
    # ... loop
    # 재귀함수

if __name__ == "__main__":
    print(factorial_loop(5))
    print(factorial_recursion(5))