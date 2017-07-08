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
    
