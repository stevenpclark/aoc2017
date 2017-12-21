def steps_to_escape(array):
    pos = 0
    steps = 0

    while True:
        steps += 1
        incr = array[pos]
        array[pos] += 1
        pos += incr
        if pos < 0 or pos >= len(array):
            return steps

assert steps_to_escape([0, 3, 0, 1, -3]) == 5

with open('input/5.txt', 'r') as f:
    array = [int(li) for li in f.readlines()]
    print(steps_to_escape(array))


