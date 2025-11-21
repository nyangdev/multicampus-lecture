# n을 입력받아 1~n까지의 숫자리스트를 만들고, 입력 받은 숫자의 약수를 출력하시오.
# lambda 사용하기!
# n = 10 이면 1,2,5,10

"""
출력결과 예시 :
숫자를 입력하시오 : 5
숫자 리스트 : [1, 2, 3, 4, 5]
약수 리스트 : [1, 5]
"""

# for 사용
user_input = int(input("숫자를 입력하시오 : "))

# 숫자 리스트 만들기
# number_list = []
#
# for i in range(1,user_input+1):
#     number_list.append(i)
#
# print(f"숫자 리스트 : {number_list}")
#
# # 약수 리스트 만들기
# div_list = []
#
# for j in range(1, user_input+1):
#     if(user_input % j == 0):
#         div_list.append(j)
#     else:
#         continue
#
# print(f"약수 리스트 : {div_list}")

# lambda 사용

# 숫자 리스트
number_list = list(map(lambda x : x, range(1, user_input + 1)))
print(f"숫자 리스트 : {number_list}")

# 약수 리스트
x = user_input
div_list = list(map(lambda y : filter(x % y == 0, number_list), number_list))
print(f"약수 리스트 : {div_list}")
