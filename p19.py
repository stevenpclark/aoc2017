if __name__ == '__main__':
    with open('19.txt', 'r') as f:
        rows = [li.strip('\n') for li in f.readlines()]

    num_rows = len(rows)
    num_cols = len(rows[0])
    for row in rows[1:]:
        assert len(row) == num_cols

    letters = []

    r = 0
    c = rows[0].index('|')

    dr = 1
    dc = 0

    steps = 0

    while True:
        steps += 1
        r += dr
        c += dc

        #print r+1,c+1

        if not(0<=r<num_rows) or not(0<=c<=num_cols):
            break

        v = rows[r][c]

        #assert v != ' ', 'ended at r=%d, c=%d'%(r+1,c+1)
        if v == ' ':
            break

        if v == '+':
            #need to change direction
            dr, dc = dc, dr
            if rows[r+dr][c+dc] == ' ':
                dr *= -1
                dc *= -1

        if 'A'<=v<='Z':
            letters.append(v)

    print(''.join(letters), steps)



