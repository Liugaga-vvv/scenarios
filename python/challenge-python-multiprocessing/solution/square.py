import multiprocessing


def square(x):

    pool = multiprocessing.Pool(processes=4)
    results = pool.map(square, range(10))
    print(results)
    return x * x
