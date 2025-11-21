from threading import Thread
from datetime import datetime
import urllib.request


def mylogger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")
    return logging

def crawling(name):
    with urllib.request.urlopen("https://www.python.org") as response:
        html = str(response.read())
        with open(f"{name}02.txt", "a") as f:
            f.write(html)

@mylogger
def func_way():
    for i in range(100):
        crawling("func")

@mylogger
def thread_way():
    threads = [Thread(target=crawling, args=("thread", )) for _ in range(100)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    func_way()
    thread_way()
    # io, network 작업 등에선 multi threading을 사용하는 것이 훨씬 빠르다