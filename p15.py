def my_gen(start, factor, criteria=None):
    prev = start
    while True:
        prev = (prev*factor)%2147483647
        if criteria is None or prev%criteria == 0:
            yield prev

def score(gen_a, gen_b, num_comparisons):
    score = 0
    for i in range(num_comparisons):
        val_a = gen_a.next()
        val_b = gen_b.next()
        if (val_a & 0xFFFF) == (val_b & 0xFFFF):
            score += 1
    return score


if __name__ == '__main__':

    print(score(my_gen(703, 16807), my_gen(516, 48271), 40000000))
    print(score(my_gen(703, 16807, 4), my_gen(516, 48271, 8), 5000000))

