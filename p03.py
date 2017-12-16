import numpy as np

def spiral(n):
    x = 0
    y = 0

    state = 0
    lim = 1
    i = 1

    while True:
        if i == n:
            return abs(x)+abs(y)
        i += 1
        if state == 0:
            x += 1
            if x >= lim:
                state = 1
        elif state == 1:
            y += 1
            if y >= lim:
                state = 2
        elif state == 2:
            x -= 1
            if x <= -lim:
                state = 3
        elif state == 3:
            y -= 1
            if y <= -lim:
                state = 0
                lim += 1

def spiral2(n):
    r = 0
    c = 0
    offset = 250

    scratch = np.zeros((500,500))
    scratch[offset, offset] = 1

    state = 0
    lim = 1

    while True:
        val = int(scratch[r+offset-1:r+offset+2,c+offset-1:c+offset+2].sum())
        scratch[r+offset,c+offset] = val
        print(val)
        if val > n:
            return val

        if state == 0:
            c += 1
            if c >= lim:
                state = 1
        elif state == 1:
            r -= 1
            if r <= -lim:
                state = 2
        elif state == 2:
            c -= 1
            if c <= -lim:
                state = 3
        elif state == 3:
            r += 1
            if r >= lim:
                state = 0
                lim += 1

print(spiral(1))
print(spiral(12))
print(spiral(23))
print(spiral(1024))
print(spiral(347991))

print(spiral2(347991))
