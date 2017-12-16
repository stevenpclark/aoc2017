def my_gen(start, factor, criteria):
    prev = start
    while True:
        prev = (prev*factor)%2147483647
        if prev%criteria == 0:
            yield prev

if __name__ == '__main__':
    genA = my_gen(703, 16807, 4)
    genB = my_gen(516, 48271, 8)

    count = 0
    for i in range(5000000):
        valA = genA.next()
        valB = genB.next()
        if (valA & 0xFFFF) == (valB & 0xFFFF):
            count += 1
    print(count)
