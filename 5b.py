def steps_to_escape(array):
    pos = 0
    steps = 0

    while True:
        steps += 1
        incr = array[pos]
        # this problem was poorly written/specified...
        # assume they aren't talking about abs(incr)
        if incr >= 3:
            array[pos] -= 1
        else:
            array[pos] += 1
        pos += incr
        if pos < 0 or pos >= len(array):
            return steps

assert steps_to_escape([0, 3, 0, 1, -3]) == 10

with open('5.txt', 'r') as f:
    array = [int(li) for li in f.readlines()]
    print(steps_to_escape(array))


