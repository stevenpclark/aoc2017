from collections import defaultdict
import sys

class Node(object):
    def __init__(self):
        self.name = None
        self.weight = None
        self.parent = None
        self.children = []


def get_total_weight(node):
    child_total_weights = [get_total_weight(c) for c in node.children]
    cw_set = set()
    for cw in child_total_weights:
        cw_set.add(cw)
    if len(cw_set) > 1:
        print 'child total weights:', child_total_weights
        print 'child immediate weights:', [c.weight for c in node.children]
        sys.exit(0)

    return sum(child_total_weights) + node.weight



node_dict = defaultdict(Node) #names to nodes

with open('input/7.txt', 'r') as f:
    for li in f.readlines():
        words = li.split()
        name = words[0]
        weight = int(words[1][1:-1])

        parent_node = node_dict[name]
        parent_node.name = name
        parent_node.weight = weight

        for child_name in words[3:]:
            child_name = child_name.replace(',', '')
            child_node = node_dict[child_name]
            child_node.name = child_name
            child_node.parent = parent_node
            parent_node.children.append(child_node)

    root_node = None
    for node in node_dict.values():
        if node.parent is None:
            root_node = node

    print(get_total_weight(root_node))





