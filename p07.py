from collections import defaultdict

class Node(object):
    def __init__(self):
        self.name = None
        self.weight = None
        self.parent = None
        self.children = []

node_dict = defaultdict(Node) #names to nodes

with open('7.txt', 'r') as f:
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

    for node in node_dict.values():
        if node.parent is None:
            print(node.name)



