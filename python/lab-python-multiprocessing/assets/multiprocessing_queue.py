import multiprocessing

def producer(queue):
    for i in range(10):
        queue.put(None)

def consumer():
    while True:
        item = None


    # TODO: implement this function
    # Note: Do not change the existing code