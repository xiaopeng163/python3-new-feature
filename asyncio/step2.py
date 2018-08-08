import time
from multiprocessing.pool import ThreadPool

def search(n):
    a,b = 0, 1
    while True:
        if len(str(a)) >= n:
            return a
        a, b = b, a + b


if __name__ == "__main__":

    t = time.time()
    pool = ThreadPool(2)
    result = pool.map(search, [3000, 4000])
    print(result)
    pool.close()
    pool.join()
    print(f'time:{time.time() - t}')
