from collections import deque

class TreeNode:

    def __init__(self, value = None, *, lc = None, rc = None):
        self.value = value
        self.lc = lc
        self.rc = rc

    @property
    def isleaf(self):
        return not self.lc and not self.rc

    @property
    def left(self):
        return self.lc

    @property
    def right(self):
        return self.rc

    @property
    def val(self):
        return self.value

Node = TreeNode

def new_bitree_level(seq):
    if not seq:
        return
    q = deque()
    it = iter(seq)
    first = next(it)
    root = Node(value = first)
    q.append(root)
    while q:
        parent = q.popleft()
        try:
            lv = next(it)
            if lv is not None:
                parent.lc = Node(lv)
                q.append(parent.lc)
            rv = next(it)
            if rv is not None:
                parent.rc = Node(rv)
                q.append(parent.rc)
        except StopIteration:
            break
    return root

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

def get_height(t):
    if not t:
        return 0
    return max(get_height(t.lc), get_height(t.rc)) + 1

def find_node_by_value(t, v):
    if not t:
        return
    if t.value == v:
        return t
    return find_node_by_value(t.lc, v) or find_node_by_value(t.rc, v)

def get_all_nodes(t):
    nodes = []
    if not t:
        return nodes
    def _pre(r):
        if not r:
            return
        nodes.append(r)
        _pre(r.lc)
        _pre(r.rc)
    _pre(t)
    return nodes

