from random import randint


'''
가위바위보 게임
출력 예)

가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 1
player (가위) vs computer(보) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 2
player (바위) vs computer(가위) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 3
player (보) vs computer(가위) : 컴퓨터가 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 4
다음에 또 놀러오세요
'''


# 가위바위보 만들기
# TODO 사용자 가위바위보 선택 받기, 컴퓨터는 1~3까지 랜덤한 수 할당
# 가위 1 바위 2 보 3

# 사용자 선택 가위
"""
컴퓨터 가위 - 비겼습니다
바위 - 컴퓨터가 이겼습니다
보 - 당신이 이겼습니다
"""

# 사용자 선택 바위
"""
컴퓨터 가위 - 당신이 이겼습니다
바위 - 비겼습니다
보 - 컴퓨터가 이겼습니다
"""

# 사용자 선택 보
"""
컴퓨터 가위 - 컴퓨터가 이겼습니다
바위 - 당신이 이겼습니다
보 - 비겼습니다
"""

# computer_choice = randint(1, 3)
# player_num = int(input("가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : "))
def game_process(player_num: int) -> None:
    """
    player - computer
    player                      가위 1 바위 2 보 3
    computer            가위 1    0       1   2
                        바위 2    -1      0   1
                        보 3     -2      -1  0

    승 : -2, 1
    무 : 0
    패 : -1, 2
    """

    prn = {1: "가위", 2: "바위", 3: "보"}

    computer_num = randint(1,3)
    print(f"player : {prn[player_num]} vs computer : {prn[computer_num]}", end= " : ")

    if(player_num - computer_num) in [-2, 1]:
        print("당신이 이겼습니다")
    elif(player_num == computer_num):
        print("비겼습니다")
    else:
        print("컴퓨터가 이겼습니다")


    # if(computer_choice == 1) :
    #     if(player_num == 1) :
    #         print("비겼습니다")
    #     elif(player_num == 2) :
    #         print("당신이 이겼습니다")
    #     elif(player_num == 3):
    #         print("컴퓨터가 이겼습니다")
    #     elif(player_num == 4):
    #         print("다음에 또 놀러오세요")
    #     else :
    #         print("비정상적인 입력으로 게임을 종료합니다")
    #
    # if(computer_choice == 2) :
    #     if(player_num == 1) :
    #         print("컴퓨터가 이겼습니다")
    #     elif(player_num == 2) :
    #         print("비겼습니다")
    #     elif(player_num == 3):
    #         print("당신이 이겼습니다")
    #     elif(player_num == 4):
    #         print("다음에 또 놀러오세요")
    #     else :
    #         print("비정상적인 입력으로 게임을 종료합니다")
    #
    # if(computer_choice == 3) :
    #     if(player_num == 1) :
    #         print("당신이 이겼습니다")
    #     elif(player_num == 2) :
    #         print("컴퓨터가 이겼습니다")
    #     elif(player_num == 3):
    #         print("비겼습니다")
    #     elif(player_num == 4):
    #         print("다음에 또 놀러오세요")
    #     else :
    #         print("비정상적인 입력으로 게임을 종료합니다")


def play() -> None:
    # game_process(player_num)
    # print("컴퓨터의 선택은 : ", computer_choice)


    while True:
        player_num = int(input("가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : "))

        if player_num == 4:
            break
        elif player_num not in [1, 2, 3]:
            print("1, 2, 3 중에 하나만 입력해 주세요")
            continue
        else:
            game_process(player_num)

    print("다음에 또 놀러오세요")


    # while True:
    #     player_num = int(input("가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : "))
    #
    #     if player_num == 4:
    #         print("다음에 또 놀러오세요")
    #         break
    #     elif player_num not in [1, 2, 3]:
    #         print("1, 2, 3 중에 하나만 입력해 주세요")
    #         continue
    #     else:0.2
    #         game_process(player_num)
    #         print("다음에 또 놀러오세요")
    #         break



if __name__ == '__main__':
    play()