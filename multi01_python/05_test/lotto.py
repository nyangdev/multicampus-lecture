from random import randint

rand_list = []
answer_list = []

# 1 ~ 45 까지의 중복되지 않는 랜덤한 숫자 6개를 정렬하여 리턴하자
def make() -> list:

    # for i in range(45) :
    #     rand_list.append(randint(1, 45))
    #
    # for i in rand_list :
    #     if i not in answer_list:
    #         answer_list.append(i)
    #         if(len(answer_list) == 6):
    #             break
    #
    # answer_list.sort()
    #
    # return answer_list

    lotto = set()
    while len(lotto) < 6:
        lotto.add(randint(1, 45))

    return sorted(lotto)

if __name__ == '__main__':
    print(make())