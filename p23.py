from collections import defaultdict

if __name__ == '__main__':
    with open('input/23.txt', 'r') as f:
        lines = f.readlines()

    cmds = [li.strip().split() for li in lines]

    pos = 0
    regs = defaultdict(int)

    #regs['a'] = 1

    mul_count = 0

    while 0<=pos<len(cmds):
        cmd = cmds[pos]
        op = cmd[0]
        x = cmd[1]
        if len(cmd) > 2:
            #sometimes y is an int, sometimes a reg name
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]

        if op == 'set':
            regs[x] = y
        elif op == 'sub':
            regs[x] -= y
        elif op == 'mul':
            mul_count += 1
            regs[x] *= y
        elif op == 'jnz':
            #handle weird case of x being '1'
            try:
                x = int(x)
            except ValueError:
                x = regs[x]
            if x != 0:
                pos += y
                continue

        pos += 1

    print mul_count
    #print regs['h']
