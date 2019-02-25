class Node:

    def __init__(self, value = None, *, lc = None, rc = None):
        self.value = value
        self.lc = lc
        self.rc = rc

def new_bitree(pre_seq, in_seq):
    root_value = pre_seq[0]
    i = 0
    while i < len(in_seq) and in_seq[i] != root_value:
        i += 1
    assert i < len(in_seq)
    node = Node(root_value)
    left_size = i
    if i > 0:
        node.lc = new_bitree(pre_seq[1:left_size+1], in_seq[0:left_size])
    if i < len(in_seq)-1:
        right_size = len(in_seq) - i + 1
        node.rc = new_bitree(pre_seq[left_size+1:], in_seq[i+1:])
    return node

def print_tree(tree):
    def _pre(t):
        if t:
            print(t.value, end = ' ')
            _pre(t.lc)
            _pre(t.rc)
    def _in(t):
        if t:
            _in(t.lc)
            print(t.value, end = ' ')
            _in(t.rc)
    print('pre: ', end = ' ')
    _pre(tree)
    print('\nin:  ', end = ' ')
    _in(tree)
    print('')

