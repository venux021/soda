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

    @left.setter
    def left(self, p):
        self.lc = p

    @property
    def right(self):
        return self.rc

    @right.setter
    def right(self, p):
        self.rc = p

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, v):
        self.value = v

class BiTree:

    @classmethod
    def new(cls, *args, **kwargs):
        return new_bitree_level(*args, **kwargs)

    @classmethod
    def show(cls, root):
        print_tree_level(root)

def new_bitree_level(seq, *, cls = TreeNode, display = False):
    Node = cls
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
    if display:
        print_tree_level(root)
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

def print_tree_level(tree):
    if not tree:
        print('Empty tree')
        return
    qu = deque([(tree,1)])
    while qu:
        node, level = qu.popleft()
        left_val = node.left.val if node.left else 'null'
        right_val = node.right.val if node.right else 'null'
        print(f'[{level}]:{node.val}:({left_val},{right_val})', end = ' ')
        if node.left:
            qu.append((node.left, level+1))
        if node.right:
            qu.append((node.right, level+1))
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

