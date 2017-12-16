with open('9.txt', 'r') as f:
    score = 0
    group_depth = 0
    garbage_count = 0
    inside_garbage = False
    ignore_next = False
    while True:
        c = f.read(1)
        if not c:
            break
        elif ignore_next:
            ignore_next = False
        elif inside_garbage:
            if c=='!':
                ignore_next = True
            elif c=='>':
                inside_garbage = False
            else:
                garbage_count += 1
        elif c=='<':
            inside_garbage = True
        elif c=='{':
            group_depth += 1
        elif c =='}':
            score += group_depth
            group_depth -= 1

    assert group_depth == 0

    print score
    print garbage_count

