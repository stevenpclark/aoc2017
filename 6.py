s = '14 0   15  12  11  11  3   5   1   6   8   4   9   1   8   4'

array = [int(s2) for s2 in s.split()]
#array = [0, 2, 7, 0]
n = len(array)

hash_set = set()

while True:
    peak_val = max(array)
    peak_ind = array.index(peak_val)
    array[peak_ind] = 0
    for i in range(peak_ind+1, peak_ind+peak_val+1):
        array[i%n] += 1
    hash_val = hash(tuple(array)) #TODO better hash later
    if hash_val in hash_set:
        print(len(hash_set)+1)
        break
    else:
        hash_set.add(hash_val)
