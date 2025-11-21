from threading import Thread

value = 0

def calc(name, start, end):
    result = 0

    for i in range(start, end):
        result += 1
        print(f"{name} : {i}")

    print(f"{name} : {result}")

    global value
    value += result

if __name__ == "__main__":
    print("hello")

    t01 = Thread(target=calc, args=["t01", 1, 50])
    t02 = Thread(target=calc, args=["t02", 50, 101])

    t01.start()
    t02.start()

    t01.join()
    t02.join()

    print(f"result = {value}")