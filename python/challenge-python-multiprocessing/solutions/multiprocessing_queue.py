import multiprocessing

def producer(queue):
    for i in range(10):
        queue.put(i)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = multiprocessing.Process(target=producer, args=(queue,))
    process_consumer = multiprocessing.Process(target=consumer, args=(queue,))
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    queue.put(None)
    process_consumer.join()
