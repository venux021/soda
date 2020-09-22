from collections import deque

class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Nary:

    @classmethod
    def new(cls, data, node_class = NaryNode):
        qu = deque()
        root = None
        parent = None
        for val in data:
            if val is not None:
                if not root:
                    root = node_class(val)
                    qu.append(root)
                else:
                    if parent.children is None:
                        parent.children = []
                    child = node_class(val)
                    parent.children.append(child)
                    qu.append(child)
            else:
                parent = qu.popleft()
        return root

    @classmethod
    def level_order(cls, root):
        if not root:
            return []
        res = [root.val, None]
        qu = deque([root])
        while qu:
            node = qu.popleft()
            for child in (node.children or []):
                res.append(child.val)
                qu.append(child)
            res.append(None)
        p = len(res) - 1
        while res[p] is None:
            p -= 1
        return res[:p+1]
