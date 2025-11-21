# 반복문을 사용하여 1 ~ 100 까지 모두 더한 결과를 출력하자
sum_hundred = 0

for number in range(1, 101):
    sum_hundred += number



print(f'1 ~ 100 까지의 결과 : {sum_hundred}')

# 반복문을 사용하여 1 ~ 100 까지 홀수합 / 짝수합을 각각 출력하자
sum_odd = 0
sum_even = 0

# 1부터 100까지 홀수합
# sum_odd = sum(filter(lambda x : x % 2 != 0, range(1,101)))
# sum_even = sum(filter(lambda x : x % 2 == 0, range(1,101)))

for x in range(1,101):
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x


print(f'홀수합 : {sum_odd}')
print(f'짝수합 : {sum_even}')
