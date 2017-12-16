import numpy as np
from p10 import get_hash_str

GRID_SZ = 128

def make_row(row_input_str):
    hash_str = get_hash_str(row_input_str)
    hash_bin_str = bin(int(hash_str, 16))[2:].zfill(GRID_SZ)
    return [int(c) for c in hash_bin_str]

def make_grid(input_str):
    grid = np.zeros((GRID_SZ,GRID_SZ), dtype=np.uint8)
    for i in range(GRID_SZ):
        row_input_str = '%s-%d'%(input_str, i)
        grid[i,:] = make_row(row_input_str)
    return grid

def count_used(input_str):
    grid = make_grid(input_str)
    return grid.sum()

def count_regions(input_str):
    grid = make_grid(input_str)

    num_groups = 0
    visited = set()

    for pos in np.ndindex(GRID_SZ,GRID_SZ):
        if visit_new_group(pos, grid, visited):
            num_groups += 1

    return num_groups

def visit_new_group(pos, grid, visited):
    #return true if this is valid and hasn't been visited yet
    r,c = pos
    if not(0<=r<GRID_SZ) or not(0<=c<GRID_SZ):
        return False

    if not grid[pos]:
        return False

    if pos in visited:
        return False

    visited.add(pos)

    visit_new_group((r+1,c), grid, visited)
    visit_new_group((r,c+1), grid, visited)
    visit_new_group((r-1,c), grid, visited)
    visit_new_group((r,c-1), grid, visited)

    return True

if __name__ == '__main__':
    #assert count_used('flqrgnkx') == 8108
    #answer1 = count_used('uugsqrei')
    #print(answer1)

    assert count_regions('flqrgnkx') == 1242
    print(count_regions('uugsqrei'))

