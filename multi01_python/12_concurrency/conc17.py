def people():
    result = list()
    while True:
        person = yield result
        result.append(person)

if __name__ == "__main__":
    co_people = people()
    next(co_people)

    print(co_people.send("홍길동"))
    print(co_people.send("이순신"))
    print(co_people.send("김선달"))