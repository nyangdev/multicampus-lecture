from numpy import character


def coroutine_sub():
    character = list()

    while True:
        char = yield

        if char is None:
            return character

        character.append(list(map(lambda x: ord(x), char)))

def coroutine():
    while True:
        character = yield from coroutine_sub()
        print(character)

if __name__ == "__main__":
    my_char = coroutine()
    next(my_char)



    my_char.send("민지")
    my_char.send("햄부기")
    my_char.send("맛있었당ㅋ")

    my_char.send(None)