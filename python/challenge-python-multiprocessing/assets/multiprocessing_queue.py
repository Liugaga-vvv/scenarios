import multiprocessing

# TODO: Implement this function and supplement the following code
# Note: Do not change the existing code

def producer(queue):
    for i in range(10):
        queue.put(None)  # The code needs to be improved here

def consumer(queue):
    while True:
        item = None  # The code needs to be improved here
        if item is None:
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = multiprocessing.Process(target=producer, args=(queue,))
    process_consumer = None  # The code needs to be improved here
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    queue.put(None)
    process_consumer.join()
