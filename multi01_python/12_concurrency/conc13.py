from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import Thread
from multiprocessing import Process
from datetime import datetime

def mylogger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")
    return logging


def calc(name):
    result = 0

    for i in range(100000000):
        result += i

    with open(f"{name}03.txt", "a") as f:
        f.write(str(result) + "\n")


@mylogger
def func_way():
    for i in range(10):
        calc("func")

@mylogger
def thread_way():
    threads = [Thread(target=calc, args=("thread", )) for _ in range(10)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

@mylogger
def process_way():
    process_list = [Process(target=calc, args=("process", )) for _ in range(10)]
    for process in process_list:
        process.start()

    for process in process_list:
        process.join()


@mylogger
def threadpool_way():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            future = executor.submit(calc, name="threadpool")
        for _ in range(10):
            future.result()


@mylogger
def processpool_way():
    with ProcessPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            future = executor.submit(calc, name="processpool")
        for _ in range(10):
            future.result()

if __name__ == "__main__":
    func_way()
    thread_way()
    process_way()
    print("------------")
    threadpool_way()
    processpool_way()