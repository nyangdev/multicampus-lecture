from threading import Thread

def bark(name, msg):
    for i in range(10):
        print(f"{name} : {msg} ({i}번지)")

if __name__ == "__main__":
    thread01 = Thread(target=bark, args=("멍멍이1", "멍멍!"))
    thread02 = Thread(target=bark, args=("멍멍이2", "멍멍!"))
    thread03 = Thread(target=bark, args=("야옹이1", "야옹!"))
    thread04 = Thread(target=bark, args=("야옹이2", "야옹!"))

    thread01.start()
    thread02.start()
    thread03.start()
    thread04.start()

    print("끝!")

    """
    thread : process 내부의 작업 단위
    process : program을 실행하여 memory에 실제로 적재된 구현체 (job, task)
    program : 코드로 이루어진 실행 가능한 파일
    """