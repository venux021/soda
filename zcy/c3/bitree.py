# -*- coding: utf-8 -*-
class BNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return not self.left and not self.right

    def str_val(self):
        return str(self.value)

def parse_bitree(s, null_str = '##', value_conv = None):
    if not value_conv:
        value_conv = lambda x: x

    def node(v):
        return BNode(value_conv(v))

    tokens = s.split(' ')
    root = node(tokens[0])
    qu = [root]
    i = 1

    while i < len(tokens) and qu:
        head = qu[0]
        del qu[0]

        if tokens[i] != null_str:
            head.left = node(tokens[i])
            qu.append(head.left)
        i += 1

        if i == len(tokens):
            break

        if tokens[i] != null_str:
            head.right = node(tokens[i])
            qu.append(head.right)
        i += 1

    return root

def pre_order_print(tree):
    def _pre(t):
        if t:
            print(t.str_val(), '', end = '')
            _pre(t.left)
            _pre(t.right)
    _pre(tree)
    print('')

def in_order_print(t):
    def _in(tree):
        if tree:
            _in(tree.left)
            print(tree.str_val(), '', end = '')
            _in(tree.right)
    _in(t)
    print('')

def level_print(t):
    if not t:
        print('Empty tree')
        return
    from collections import deque
    q = deque()
    q.append((t, 1))
    level = 1
    while q:
        head = q.popleft()
        if head[1] > level:
            print()
            level = head[1]
        if head[0]:
            print(head[0].value, '', end = '')
            q.append((head[0].left, head[1]+1))
            q.append((head[0].right, head[1]+1))
        else:
            print('## ', end = '')

    print()
    
