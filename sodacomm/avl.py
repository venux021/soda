class AVLNode:

    def __init__(self, val):
        self.val = val
        self.height = 0
        self.bf = 0
        self.left = self.right = None

class AVLTree:

    def __init__(self, node_class = AVLNode):
        self.root = None
        self.node_class = node_class

    def insert(self, val):
        self.root = self.do_insert(self.root, val)

    def lower_bound(self, val):
        upper = None
        p = self.root
        while p:
            if val == p.val:
                return val
            elif val < p.val:
                upper = p
                p = p.left
            else:
                p = p.right
        return upper.val if upper else None

    def upper_bound(self, val):
        upper = None
        p = self.root
        while p:
            if val == p.val:
                if p.right:
                    q = p.right
                    while q.left:
                        q = q.left
                    return q.val
                else:
                    break
            elif val < p.val:
                upper = p
                p = p.left
            else:
                p = p.right
        return upper.val if upper else None

    def create_node(self, val):
        return self.node_class(val)

    def with_duplicate(self, node):
        pass

    def do_insert(self, node, val):
        if not node:
            return self.create_node(val)
        elif val == node.val:
            self.with_duplicate(node)
            return node
        elif val < node.val:
            node.left = self.do_insert(node.left, val)
        else: # val > node.val:
            node.right = self.do_insert(node.right, val)
        return self.balance(node)

    def update_height(self, node) -> int:
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        node.height = max(left_height, right_height) + 1
        node.bf = left_height - right_height

    def balance(self, node) -> None:
        self.update_height(node)
        if node.bf > 1:
            if node.left.bf < 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif node.bf < -1:
            if node.right.bf > 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node

    def rotate_left(self, node):
        a = node; b = a.right; c = b.left
        a.right = c
        b.left = a
        self.update_height(a)
        self.update_height(b)
        return b

    def rotate_right(self, node):
        a = node; b = a.left; c = b.right
        a.left = c
        b.right = a
        self.update_height(a)
        self.update_height(b)
        return b
