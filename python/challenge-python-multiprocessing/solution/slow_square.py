import multiprocessing
import time

def slow_square(x):
    time.sleep(1)
    return x * x

def callback(result):
    print(result)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    results = [pool.apply_async(slow_square, (x,), callback=callback) for x in range(10)]
    for result in results:
        result.wait()
