from operator import xor
from itertools import izip_longest
import struct

def grouper(iterable, n, fillvalue=None):
    #from itertools docs
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def flip(array, pos, n):
    #modifies array in-place
    array_len = len(array)
    for i in range(n/2):
        p1 = (pos+i)%array_len
        p2 = (pos+n-1-i)%array_len
        array[p1], array[p2] = array[p2], array[p1]


def twist_me(array, twist_lens, iterations=1):
    #modifies array in-place
    array_len = len(array)
    pos = 0
    skip_size = 0
    for it in range(iterations):
        for tlen in twist_lens:
            flip(array, pos, tlen)
            pos = (pos + tlen + skip_size)%array_len
            skip_size += 1

    return array


if __name__ == '__main__':
    assert twist_me([0,1,2,3,4], [3,4,1,5]) == [3,4,2,1,0]

    with open('10.txt', 'r') as f:
        input_str = f.readline().strip()

    #part 1
    array = range(256)
    twist_lens = [int(s) for s in input_str.split(',')]
    twist_me(array, twist_lens, iterations=1)
    print(array[0]*array[1])

    #part 2
    array = range(256)
    twist_lens = [ord(c) for c in input_str]
    twist_lens.extend([17, 31, 73, 47, 23])
    twist_me(array, twist_lens, iterations=64)

    dense_hash = [reduce(xor, chunk) for chunk in grouper(array, 16)]
    hash_str = struct.pack('B'*16, *dense_hash)
    print(hash_str.encode('hex'))
