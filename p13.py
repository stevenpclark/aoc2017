class Scanner(object):
    def __init__(self, depth, span):
        self.depth = depth
        self.span = span
        self._period = 2*(span-1)

    def at_zero(self, t):
        return t%self._period == 0


def get_min_safe_delay(scanners):
    delay = 0
    while True:
        for scanner in scanners:
            if scanner.at_zero(delay+scanner.depth):
                #caught!
                break
        else:
            #made it all the way through
            return delay
        delay += 1


if __name__ == '__main__':
    depths = []
    spans = []
    with open('input/13.txt', 'r') as f:
        for li in f.readlines():
            s_depth, s_span = li.split(':')
            depths.append(int(s_depth))
            spans.append(int(s_span))
    #depths = [0,1,4,6]
    #spans = [3,2,4,4]

    scanners = [Scanner(d,s) for d,s in zip(depths, spans)]

    print(get_min_safe_delay(scanners))



