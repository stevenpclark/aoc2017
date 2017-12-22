import numpy as np

CLEAN, WEAKENED, INFECTED, FLAGGED = range(4)

def lines_to_grid(lines):
    return np.array([[c=='#' for c in li] for li in lines], dtype=int)*INFECTED


char_formatter = lambda x:{False:'.', True:'#'}[x]

def grid_to_str(grid):
    return np.array2string(grid, formatter={'bool':char_formatter}, separator='')

if __name__ == '__main__':
    with open('input/22.txt', 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    small_grid = lines_to_grid(lines)
    small_rows, small_cols = small_grid.shape

    #paste small grid into center of a big grid
    big_size = 1001
    grid = np.zeros((big_size, big_size), dtype=int)
    small_start_row = big_size/2-small_rows/2
    small_start_col = big_size/2-small_cols/2
    grid[small_start_row:small_start_row+small_rows, small_start_col:small_start_col+small_cols] = small_grid

    #increasing index = R turn
    #decreasing index = L turn
    headings = ((-1,0), (0,1), (1,0), (0,-1))
    h_ind = 0 #start facing UP

    num_rows, num_cols = grid.shape

    r = num_rows/2
    c = num_cols/2

    #print(grid_to_str(grid))
    #print(grid.shape)

    num_new_infections = 0

    for i in xrange(10000000):
        assert 0<=r<num_rows
        assert 0<=c<num_cols

        v = grid[r,c]
        if v == CLEAN:
            h_ind -= 1 #turn left
        elif v == WEAKENED:
            #no turn, h_ind stays same
            num_new_infections += 1 #going to infect
        elif v == INFECTED:
            h_ind += 1 #turn right
        else:
            h_ind += 2 #reverse

        grid[r,c] = (v+1)%4
        h_ind = h_ind % 4
        dr, dc = headings[h_ind]
        r += dr
        c += dc

    print(num_new_infections)


