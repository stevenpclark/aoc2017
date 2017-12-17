#python3 only!
import numpy as np
from tqdm import tqdm

def print_a(a, count):
    x = 0
    for i in range(count):
        print(x, end=' ')
        x = a[x]
    print()

if __name__ == '__main__':
    x = 0
    #step = 3
    #n = 10
    step = 359
    n = 50000000
    a = np.zeros(n+1, dtype=int)
    for val in tqdm(range(1,n+1)):
        #print('curr_node:', x)
        #print_a(a, val)
        for i in range(step):
            x = a[x]
        #append val after x
        #set val's child to x's child
        #set x's child to val
        #set x to val

        a[val] = a[x]
        a[x] = val
        x = val
        #print(a)

    print(a[0])

