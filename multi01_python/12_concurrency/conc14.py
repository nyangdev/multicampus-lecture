from concurrent.futures import ThreadPoolExecutor
from threading import Thread

def return_calc():
    result = 0
    for i in range(10):
        result += i
    return result

def non_return_calc():
    result = 0
    for i in range(10):
        result += i
    print(f"result : {result}")

def thread_way():
    # Thread
    # 하나의 객체 당 하나의 작업만 관리 가능
    # 리턴되는 결과 확인 불가
    # 작업 상태 확인 불가
    thread01 = Thread(target=return_calc)
    thread02 = Thread(target=non_return_calc)

    thread01.start()
    thread02.start()

    thread01.join()
    thread02.join()

    print(thread01)
    print(thread02)

def threadpool_way():
    # ThreadPoolExecutor
    # 하나의 객체로 여러 개의 작업 관리 가능
    # return 되는 값 확인 가능
    # 작업 상태(status) 확인 가능
    # 추가적인 기능들이 더 있음
    with ThreadPoolExecutor(max_workers=2) as executor:
        future01 = executor.submit(return_calc)
        future02 = executor.submit(non_return_calc)

        print(future01.result())
        print(future02.result())

        print(future01)
        print(future02)

if __name__ == "__main__":
    thread_way()
    print("--------------")
    threadpool_way()