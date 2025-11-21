def generator01(end):
    yield list(range(end))

def generator02(end):
    # yield from
    # 다른 generator 호출
    yield from list(range(end))

if __name__ == "__main__":
    gen01 = generator01(10)
    for item in gen01:
        print(item)

    print("---------")
    gen02 = generator02(10)
    for item in gen02:
        print(item)