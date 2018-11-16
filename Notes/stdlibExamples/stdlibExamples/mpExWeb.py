import time
from multiprocessing import pool


def expensiveCalculation(x):
    print('Processing {}'.format(x))
    time.sleep(x)
    return x**2


def main():
    xs = list(range(10))
    
    t1 = time.time()
    # Fun Fact: map deffers execution untill the result is asked for.
    mapResult = list(map(expensiveCalculation, xs))
    tDelta = time.time() - t1
    
    print('Elapsed Time: {}'.format(tDelta))
    print(mapResult)

    t1 = time.time()
    with pool.Pool() as p:
        mapResult = p.map(expensiveCalculation, xs)
    tDelta = time.time() - t1
    
    print('Elapsed Time: {}'.format(tDelta))
    print(list(mapResult))

if __name__ == '__main__':
    main()