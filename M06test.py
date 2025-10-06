from multiprocessing import Process
import random
from datetime import datetime
from time import sleep
def kinda_times():
    sleep(random.random())
    print(datetime.strftime(datetime.today(), "%H:%M:%S:%f"))
if __name__ == '__main__':
    processes = []
    for x in range(3):
        p = Process(target=kinda_times)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
        print("Processes completed.")