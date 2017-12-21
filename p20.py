from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    with open('input/20.txt', 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    n = len(lines)

    pos = np.zeros((n, 3))
    vel = np.zeros((n, 3))
    acc = np.zeros((n, 3))

    for i, li in enumerate(lines):
        #TODO regex
        li = li.replace('p=<', '')
        li = li.replace('>, v=<', ',')
        li = li.replace('>, a=<', ',')
        li = li.replace('>', '')
        nums = [int(s) for s in li.split(',')]
        pos[i,:] = nums[0:3]
        vel[i,:] = nums[3:6]
        acc[i,:] = nums[6:9]

    for i in range(1000):
        #should probably use np.unique or something else for this...
        row_map = defaultdict(list)
        for j, row in enumerate(pos):
            if np.inf not in row:
                row_map[tuple(row)].append(j)
        for k,v in row_map.iteritems():
            if len(v) > 1:
                pos[v,:] = np.inf

        vel += acc
        pos += vel

    if 0:
        dist = np.sum(abs(pos), axis=1)
        print(dist.argmin())
    else:
        print(sum(pos[:,0] != np.inf))



