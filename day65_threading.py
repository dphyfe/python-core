# Day 65: threading basics for my practice

import threading
import time

def my_worker(name, delay):
    print(f"My {name} starting")
    time.sleep(delay)
    print(f"My {name} finished")

my_t1 = threading.Thread(target=my_worker, args=("worker-1", 0.1))
my_t2 = threading.Thread(target=my_worker, args=("worker-2", 0.1))

my_t1.start()
my_t2.start()

my_t1.join()
my_t2.join()
print("My both threads done")

my_counter = 0
my_lock = threading.Lock()

def my_increment():
    global my_counter
    for _ in range(100000):
        with my_lock:
            my_counter += 1

my_threads = [threading.Thread(target=my_increment) for _ in range(2)]
for t in my_threads:
    t.start()
for t in my_threads:
    t.join()

print(f"My counter: {my_counter}")

my_event = threading.Event()

def my_waiter():
    print("My waiting for event")
    my_event.wait()
    print("My event received")

my_t3 = threading.Thread(target=my_waiter)
my_t3.start()
time.sleep(0.1)
my_event.set()
my_t3.join()

my_data = threading.local()

def my_thread_func():
    my_data.value = threading.current_thread().name
    print(f"My thread data: {my_data.value}")

my_t4 = threading.Thread(target=my_thread_func, name="My-Thread-1")
my_t5 = threading.Thread(target=my_thread_func, name="My-Thread-2")
my_t4.start()
my_t5.start()
my_t4.join()
my_t5.join()

print(f"My active threads: {threading.active_count()}")
print(f"My current thread: {threading.current_thread().name}")
