from multiprocessing import Process
from time import sleep


def daemon_process():
    while True:print("♥")
    sleep(1)

def work_process():
    print("work start")
    daemon = Process(target=daemon_process)
    daemon.daemon = True
    daemon.start()
    sleep(5)
    print("work stop")

if __name__ == "__main__":
    work_process()