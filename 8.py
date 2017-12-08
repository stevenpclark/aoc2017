from collections import defaultdict

regs = defaultdict(int)
max_val = 0

with open('8.txt', 'r') as f:
    for li in f.readlines():
        w = li.split()
        if w[1] == 'inc':
            w[1] = '+='
        else:
            w[1] = '-='
        cmd = 'if regs["%s"] %s %s: regs["%s"]%s%s'%(w[4], w[5], w[6], w[0], w[1], w[2])
        exec(cmd)
        max_val = max(max_val, regs[w[0]])

print('max current:', max(regs.values()))
print('max ever seen:', max_val)
