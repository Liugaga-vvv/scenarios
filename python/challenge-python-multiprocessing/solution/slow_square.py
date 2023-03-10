import multiprocessing
import time

def slow_square(x):
    time.sleep(1)
    return x * x

def callback(result):
    print(result)


    pool = multiprocessing.Pool(processes=4)
    results = [pool.apply_async(slow_square, (x,), callback=callback) for x in range(10)]
    for result in results:
        result.wait()
    print("All tasks completed.")