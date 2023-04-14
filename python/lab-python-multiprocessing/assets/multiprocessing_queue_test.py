import sys

sys.path.append("/home/labex/project")

import unittest
import multiprocessing
from multiprocessing_queue import producer, consumer


class TestMultiprocessing(unittest.TestCase):
    def test_producer_consumer(self):
        queue = multiprocessing.Queue()
        process_producer = multiprocessing.Process(target=producer, args=(queue,))
        process_consumer = multiprocessing.Process(target=consumer, args=(queue,))
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        queue.put(None)
        process_consumer.join()
        self.assertEqual(queue.qsize(), 0)


if __name__ == "__main__":
    unittest.main()
