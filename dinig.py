import threading
import time
import random

forks = [threading.Lock() for _ in range(5)]

def philosopher(i):
    left_fork = forks[i]
    right_fork = forks[(i + 1) % 5]

    while True:
        time.sleep(random.random())
        left_fork.acquire()
        time.sleep(random.random())
        right_fork.acquire()

        print(f"Philosopher {i} eating")
 
        right_fork.release()
        left_fork.release()

        print(f"Philosopher {i} thinking")

philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(5)]

for philosopher_thread in philosopher_threads:
    philosopher_thread.start()

for philosopher_thread in philosopher_threads:
    philosopher_thread.join()
