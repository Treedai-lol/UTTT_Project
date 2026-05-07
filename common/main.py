from copy import deepcopy
from time import perf_counter

def main():
    raw = [1,2,3,4,5]
    new = []
    for i in range(5):
        new.append(raw[i])
    new[2] = 67
    print(raw)
    print(new)
if __name__ == '__main__':
    main()