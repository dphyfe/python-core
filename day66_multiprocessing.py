# Day 66: multiprocessing basics for my practice

from multiprocessing import Process, Queue, Pool
import os
import time

def my_worker(name):
    print(f"My {name} in process {os.getpid()}")
    time.sleep(0.1)
    print(f"My {name} done")

if __name__ == "__main__":
    my_p1 = Process(target=my_worker, args=("worker-1",))
    my_p2 = Process(target=my_worker, args=("worker-2",))
    
    my_p1.start()
    my_p2.start()
    
    my_p1.join()
    my_p2.join()
    print("My processes done")

def my_square(x):
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as my_pool:
        my_results = my_pool.map(my_square, [1, 2, 3, 4, 5])
        print(f"My results: {my_results}")

def my_producer(q):
    for i in range(5):
        q.put(f"My item {i}")
    q.put(None)

def my_consumer(q):
    while True:
        my_item = q.get()
        if my_item is None:
            break
        print(f"My consumed: {my_item}")

if __name__ == "__main__":
    my_queue = Queue()
    my_prod = Process(target=my_producer, args=(my_queue,))
    my_cons = Process(target=my_consumer, args=(my_queue,))
    
    my_prod.start()
    my_cons.start()
    
    my_prod.join()
    my_cons.join()
    print("My queue example done")

from multiprocessing import Value, Array

def my_increment(shared_val):
    for _ in range(100):
        with shared_val.get_lock():
            shared_val.value += 1

if __name__ == "__main__":
    my_val = Value('i', 0)
    my_processes = [Process(target=my_increment, args=(my_val,)) for _ in range(2)]
    
    for p in my_processes:
        p.start()
    for p in my_processes:
        p.join()
    
    print(f"My shared value: {my_val.value}")

# Progress: part 2/2
