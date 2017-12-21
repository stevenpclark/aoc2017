from collections import defaultdict

if __name__ == '__main__':
    with open('input/18.txt', 'r') as f:
        lines = f.readlines()

    cmds = [li.strip().split() for li in lines]

    pos = 0
    regs = defaultdict(int)
    last_sound = None

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

        if op == 'snd':
            last_sound = regs[x]
        elif op == 'set':
            regs[x] = y
        elif op == 'add':
            regs[x] += y
        elif op == 'mul':
            regs[x] *= y
        elif op == 'mod':
            regs[x] = regs[x] % y
        elif op == 'rcv':
            if regs[x] != 0:
                print(last_sound)
                break
        elif op == 'jgz':
            if regs[x] > 0:
                pos += y
                continue

        pos += 1


