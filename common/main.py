from copy import deepcopy
from time import perf_counter

def main():
    t1 = perf_counter()
    a = 10
    for i in range(1000000):
        b = deepcopy(a)
    print(perf_counter()-t1)
if __name__ == '__main__':
    main()