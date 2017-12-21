with open('input/4.txt', 'r') as f:
    lines = f.readlines()
    num_valid = 0
    for li in lines:
        words = li.split()
        words = [''.join(sorted(list(w))) for w in words]
        if len(words) == len(set(words)):
            num_valid += 1
    print num_valid
