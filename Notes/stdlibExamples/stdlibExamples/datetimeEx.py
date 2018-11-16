import datetime as dt
import time

def main():
    for _ in range(100000):
        print('\r{}'.format(dt.datetime.now()), end='')
    print()
    d1 = dt.datetime.now()
    time.sleep(5)
    d2 = dt.datetime.now()
    print(d2 - d1)
    # is d1 before d2?
    print('Is {} before {}? {}'.format(d1, d2, (d1<d2)))

if __name__ == '__main__':
    main()