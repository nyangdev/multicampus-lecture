import pickle

# with 구문은 자동으로 close 해줌
# with 구문 사용하는 것이 훨씬 효율적
with open("test02.txt", "rb") as file:
    score = pickle.load(file)
    print(score)


# with 구문 안에서 만들어진 변수도 외부에서 사용 가능하다
print(score)