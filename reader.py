import threading
import time
import random

buffer = []
readers_count = 0
write_lock = threading.Lock()
read_lock = threading.Lock()

def reader():
    global readers_count
    while True:
        time.sleep(random.random())  # Simulate reading time
        with read_lock:
            readers_count += 1
            if readers_count == 1:
                write_lock.acquire()
        # Reading
        print(f"Reading: {buffer}")
        with read_lock:
            readers_count -= 1
            if readers_count == 0:
                write_lock.release()

def writer():
    while True:
        time.sleep(random.random())  # Simulate writing time
        with write_lock:
            # Writing
            buffer.append(random.randint(1, 100))
            print(f"Writing: {buffer}")

# Create reader threads
reader_threads = [threading.Thread(target=reader) for _ in range(3)]
# Create writer thread
writer_thread = threading.Thread(target=writer)

# Start threads
for reader_thread in reader_threads:
    reader_thread.start()
writer_thread.start()

# Join threads
for reader_thread in reader_threads:
    reader_thread.join()
writer_thread.join()
