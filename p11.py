# I had previously bookmarked https://www.redblobgames.com/grids/hexagons/
# which was a handy reference

import numpy as np

cube_dirs = {
    'n': np.array([0,1,-1]),
    's': np.array([0,-1,1]),
    'ne': np.array([1,0,-1]),
    'sw': np.array([-1,0,1]),
    'nw': np.array([-1,1,0]),
    'se': np.array([1,-1,0])
}

def dist_from_origin(pos):
    return max(abs(pos))

with open('input/11.txt', 'r') as f:
    dirs = f.readline().strip().split(',')

max_dist = 0
pos = np.array([0,0,0])
for d in dirs:
    pos += cube_dirs[d]

    dist = dist_from_origin(pos)
    max_dist = max(max_dist, dist)

print(dist)
print(max_dist)

