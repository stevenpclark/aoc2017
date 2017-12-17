#python3 only!
from tqdm import tqdm

#use circular linked list
class Node(object):
    def __init__(self, x, parent=None):
        self.x = x
        if parent:
            self.next = parent.next
            parent.next = self
        else:
            self.next = self

def print_nodes(node, count):
    for i in range(count):
        print(node.x, end=' ')
        node = node.next
    print()

if __name__ == '__main__':
    zero = Node(0)
    curr_node = zero
    step = 359
    n = 50000000
    for val in tqdm(range(1,n+1)):
        #print('curr_node:', curr_node.x)
        #print_nodes(zero, val)
        for i in range(step):
            curr_node = curr_node.next
        curr_node = Node(val, curr_node)

    print(zero.next.x)

