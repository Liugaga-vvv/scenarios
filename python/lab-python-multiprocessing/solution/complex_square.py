import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(1000000))
    print(results[:10])