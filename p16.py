#python3 only! range vs. xrange

if __name__ == '__main__':

    a = list('abcdefghijklmnop')
    op_list = []
    operands_list = []


    with open('input/16.txt', 'r') as f:
        moves = f.readline().strip().split(',')

    for move in moves:
        op = move[0]
        operands = move[1:].split('/')
        if op == 's':
            operands = tuple([int(operands[0])])
        elif op == 'x':
            operands = tuple([int(operands[0]), int(operands[1])])
        elif op == 'p':
            operands = tuple([operands[0], operands[1]])
        op_list.append(move[0])
        operands_list.append(operands)

    seen = set()
    results = []
    period = 0

    for i in range(1000000000):
        for op, operands in zip(op_list, operands_list):
            if op == 's':
                n = operands[0]
                a = a[-n:]+a[:-n]
            elif op == 'x':
                n1, n2 = operands
                a[n1], a[n2] = a[n2], a[n1]
            else: #op is 'p'
                p1, p2 = operands
                n1 = a.index(p1)
                n2 = a.index(p2)
                a[n1], a[n2] = a[n2], a[n1]
        result = ''.join(a)
        if result in seen:
            period = i
            break
        else:
            seen.add(result)
            results.append(result)

    print(period)

    print(results[(1000000000-1)%period])

