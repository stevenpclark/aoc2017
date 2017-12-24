from math import sqrt

#in the end, it boils down to prime finding...

if __name__ == '__main__':
    h=0
    for b in range(109300, 126301, 17):
        prime = True

        for d in xrange(2, 1+int(sqrt(b))):
            if b%d == 0:
                prime = False
                break

        #print b, prime
        if not prime:
            h += 1

    print h
