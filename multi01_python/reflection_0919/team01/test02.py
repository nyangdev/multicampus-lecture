# 홀수와 짝수 개수 구하기

number = [2, 43, 1, 6, 94, 76, 193, 0]

even = 0
odd = 0

# 반복문

for num in number:
    # print(num)
    if(num % 2 == 0):
        even += 1
    else:
        odd += 1


print(f"홀수 : {odd} 개 \t 짝수 : {even} 개")