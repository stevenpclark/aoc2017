from collections import namedtuple
from operator import attrgetter

Result = namedtuple('Result', ['strength', 'length'])

strength_first = attrgetter('strength', 'length')
length_first = attrgetter('length', 'strength')

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.strength = a+b

    def get_opposite_port(self, x):
        #if pair doesn't contain x, return None
        #else, return opposite half
        if self.a == x:
            return self.b
        elif self.b == x:
            return self.a
        else:
            return None

def optimize(start_port, unused_pairs, memo, max_key):
    #break into sub-problems (dynamic programming), use memoization
    #allow for different sorting preferences via max_key
    memo_key = tuple([start_port, tuple(unused_pairs)])
    if memo_key in memo:
        return memo[memo_key]

    results = [Result(0,0)]
    #check out all unused ports that match
    for pair in unused_pairs:
        next_port = pair.get_opposite_port(start_port)
        if next_port is not None:
            remaining_unused = unused_pairs[:]
            remaining_unused.remove(pair)
            child_result = optimize(next_port, remaining_unused, memo, max_key)
            new_strength = child_result.strength+pair.strength
            new_length = child_result.length + 1
            results.append(Result(new_strength, new_length))

    max_val = max(results, key=max_key)
    memo[memo_key] = max_val
    return max_val


if __name__ == '__main__':
    with open('input/24.txt', 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    unused_pairs = []
    for li in lines:
        words = li.split('/')
        unused_pairs.append(Pair(int(words[0]), int(words[1])))

    memo = {}
    print(optimize(0, unused_pairs, memo, max_key=strength_first))

    memo = {}
    print(optimize(0, unused_pairs, memo, max_key=length_first))

