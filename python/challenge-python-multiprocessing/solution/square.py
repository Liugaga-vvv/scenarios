import multiprocessing

def square(x):
    return x * x

    pool = multiprocessing.Pool(processes=4)
    results = pool.map(square, range(10))
    print(results)