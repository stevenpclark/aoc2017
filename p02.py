with open('input/2.txt', 'r') as f:
    total = 0
    for li in f.readlines():
        nums = [int(s) for s in li.split()]
        nums.sort(reverse=True)

        matched = False
        for i,nbig in enumerate(nums):
            for nsmall in nums[i+1:]:
                if nbig%nsmall == 0:
                    matched = True
                    total += nbig/nsmall
                    break
            if matched:
                break

    print total

