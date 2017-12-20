from collections import defaultdict
from queue import Queue, Empty
import threading

def run(p, cmds, q_in, q_out):
    pos = 0
    regs = defaultdict(int)
    regs['p'] = p

    send_cmds = 0

    positions = defaultdict(int)


    while 0<=pos<len(cmds):
        positions[pos] += 1
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
            q_out.put(regs[x])
            send_cmds += 1
        elif op == 'set':
            regs[x] = y
        elif op == 'add':
            regs[x] += y
        elif op == 'mul':
            regs[x] *= y
        elif op == 'mod':
            regs[x] = regs[x] % y
        elif op == 'rcv':
            try:
                y = int(q_in.get(block=True, timeout=3))
                regs[x] = y
            except Empty:
                break
        elif op == 'jgz':
            #handle weird case of x being '1'
            try:
                x = int(x)
            except ValueError:
                x = regs[x]
            if x > 0:
                pos += y
                continue

        pos += 1
    print('program %d exited, sent %d' % (p, send_cmds))


if __name__ == '__main__':
    with open('18.txt', 'r') as f:
        lines = f.readlines()

    cmds = [li.strip().split() for li in lines]

    q_a = Queue()
    q_b = Queue()

    workers = []
    workers.append(threading.Thread(target=run, args=(0, cmds, q_a, q_b)))
    workers.append(threading.Thread(target=run, args=(1, cmds, q_b, q_a)))

    print('starting workers')
    for worker in workers:
        worker.start()

    print('waiting for workers')
    for worker in workers:
        worker.join()


