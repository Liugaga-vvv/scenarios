import multiprocessing
import time


def slow_square(x):
    time.sleep(None)
    return None


def callback(result):
    print(result)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    results = None
    for result in results:
        result.wait()

    # TODO: implement this function
    # Note: Do not change the existing code
