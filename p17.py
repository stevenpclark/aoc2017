if __name__ == '__main__':
    a = [0]
    pos = 0
    step = 359
    n = 2017
    for val in range(1,n+1):
        #val is also the length of a at top of loop
        pos = (pos+step)%val
        a.insert(pos+1, val)
        pos += 1

    final_index = a.index(n)
    answer_index = (final_index+1)%len(a)
    print(a[answer_index])

