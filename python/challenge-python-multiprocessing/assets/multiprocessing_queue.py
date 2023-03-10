import multiprocessing

def producer(queue):
    for i in range(10):
        queue.put(None)

def consumer(queue):
    while True:
        item = queue.get()


    # TODO: implement this function
    # Note: Do not change the existing code