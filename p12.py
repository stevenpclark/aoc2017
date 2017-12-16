from collections import defaultdict

child_dict = defaultdict(list) #int to list of ints

untagged_set = set()
with open('12.txt', 'r') as f:
    for li in f.readlines():
        left, right = li.split(' <-> ')
        parent = int(left)
        child_list = [int(s) for s in right.split(',')]
        child_dict[parent] = child_list
        untagged_set.add(parent)

def tag(n, tag_set):
    if n in tag_set:
        return False
    tag_set.add(n)
    for child in child_dict[n]:
        tag(child, tag_set)
    return True

tag_set = set()
tag(0, tag_set)
print(len(tag_set))

num_groups = 1
for i in child_dict.keys():
    if tag(i, tag_set):
        num_groups += 1

print(num_groups)
