import numpy as np

def str_to_grid(s):
    #convert e.g. '#./.#' to a 2x2 np boolean array
    #python is awesome.
    return np.array([[c=='#' for c in row] for row in s.split('/')], dtype=bool)

char_formatter = lambda x:{False:'.', True:'#'}[x]

def grid_to_str(grid):
    return np.array2string(grid, formatter={'bool':char_formatter}, separator='')


def make_rules(lines):
    #return dictionary of ravel-tuple to np array
    d = dict()
    for li in lines:
        chunk_strs = li.split(' => ')
        input_chunk = str_to_grid(chunk_strs[0])
        output_chunk = str_to_grid(chunk_strs[1])

        for i in range(4):
            d[tuple(input_chunk.ravel())] = output_chunk
            d[tuple(np.fliplr(input_chunk).ravel())] = output_chunk
            input_chunk = np.rot90(input_chunk)

    return d


def run_grid(grid, rules, num_iterations):
    for i in range(num_iterations):
        grid = get_next_grid(grid, rules)

    return grid


def get_next_grid(input_grid, rules):
    input_grid_size = input_grid.shape[0]
    if input_grid_size % 2 == 0:
        input_chunk_size = 2
        output_chunk_size = 3
    else:
        input_chunk_size = 3
        output_chunk_size = 4
    num_chunks = input_grid_size / input_chunk_size
    output_grid_size = num_chunks*output_chunk_size

    output_grid = np.zeros((output_grid_size, output_grid_size), dtype=bool)

    for r in range(num_chunks):
        for c in range(num_chunks):
            input_chunk = input_grid[r*input_chunk_size:(r+1)*input_chunk_size, c*input_chunk_size:(c+1)*input_chunk_size]
            output_chunk = rules[tuple(input_chunk.ravel())]
            output_grid[r*output_chunk_size:(r+1)*output_chunk_size, c*output_chunk_size:(c+1)*output_chunk_size] = output_chunk

    return output_grid


if __name__ == '__main__':
    with open('input/21.txt', 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    #lines = ['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#']
    rules = make_rules(lines)

    grid = str_to_grid('.#./..#/###')

    grid = run_grid(grid, rules, 18)

    #print(grid_to_str(grid))
    print(grid.sum())


