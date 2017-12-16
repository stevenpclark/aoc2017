#python3 only! range vs. xrange

from tqdm import tqdm

if __name__ == '__main__':

    a = list('abcdefghijklmnop')
    op_list = []
    operands_list = []

    with open('16.txt', 'r') as f:
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

    for i in tqdm(range(1000000000)):
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

    print(''.join(a))


