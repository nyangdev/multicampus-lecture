from threading import Thread
from time import sleep

value = 10

def calc(name, num, sleep_time):
    global value
    for i in range(10):
        value = value + num
        print(f"{name}{i} : {value}")
        sleep(sleep_time)

if __name__ == "__main__":
    print("main thread start")
    test = Thread(target=calc, args=["test", 1, 0.5])
    daemon = Thread(target=calc, args=("daemon", -1, 1))

    # daemon.setDaemon(True)
    daemon.daemon = True
    # daemon Thread
    # thread를 보조하는 thread
    # daemon이 아닌 thread가 더 이상 없을때 종료된다

    test.start()
    daemon.start()

    print(f"test.isDaemon : {test.daemon}")
    print(f"daemon.isDaemon : {daemon.daemon}")
    # print(f"daemon.isDaemon : {daemon.isDaemon}")

    print("main thread end")