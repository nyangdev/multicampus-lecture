# 반복문과 lambda를 사용하여 학생 각각의 총점과 평균을 출력하자
students = [{'name': '홍길동', 'kor': 100, 'eng': 70, 'math': 89},
            {'name': '이순신', 'kor': 66, 'eng': 87, 'math': 100},
            {'name': '김선달', 'kor': 91, 'eng': 100, 'math': 84}]

'''
출력결과

[홍길동]
총점 : 259 	 평균 : 86.33
[이순신]
총점 : 253 	 평균 : 84.33
[김선달]
총점 : 275 	 평균 : 91.67
'''

def myfunc(x):
    return type(x) == int


for student in students:
    print(f"[ {student["name"]} ]")
    #score = list(filter(lambda x: type(x) == int, student.values()))
    score = list(filter(myfunc, student.values()))

    score_sum = sum(score)
    score_avg= score_sum / len(score)
    print(f"총점 : {score_sum} \t 평균 : {score_avg:.2f}")