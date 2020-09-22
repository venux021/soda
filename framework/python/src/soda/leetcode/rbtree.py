class RBNode:

    __slots__ = ['key','val','parent','left','right','red']

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.left = self.right = None
        self.red = False

Nil = RBNode(None, None)

class RBTree:

    def __init__(self):
        self.root = Nil

    def insert(self, key, val):
        x = self.root
        y = Nil
        while x != Nil:
            y = x
            if key == x.key:
                x.val = val
                return False
            if key < x.key:
                x = x.left
            else:
                x = x.right

        t = RBNode(key, val)
        t.left = t.right = Nil
        t.parent = y

        if y == Nil:
            self.root = t
        elif key < y.key:
            y.left = t
        else:
            y.right = t

        t.red = True
        self._insert_fixup(t)
        return True

    def find(self, key):
        p = self.root
        while p != Nil:
            if key == p.key:
                return p.val
            elif key < p.key:
                p = p.left
            else:
                p = p.right
        return None

    def _insert_fixup(self, z):
        zp = zpp = None
        while z.parent.red:
            zp = z.parent
            zpp = zp.parent
            if zp == zpp.left:
                zu = zpp.right  # uncle of z
                if zu.red:
                    zp.red = zu.red = False
                    zpp.red = True
                    z = zpp
                else:
                    # zu is black
                    if z == zp.right:
                        z = zp
                        self.rotate_left(z)
                        zp = z.parent
                    zp.red = False
                    zpp.red = True
                    self.rotate_right(zpp)
            else:
                # zp is right child of zpp
                zu = zpp.left
                if zu.red:
                    zp.red = zu.red = False
                    zpp.red = True
                    z = zpp
                else:
                    # zu is black
                    if z == zp.left:
                        z = zp
                        self.rotate_right(z)
                        zp = z.parent
                    zp.red = False
                    zpp.red = True
                    self.rotate_left(zpp)
        self.root.red = False

    def rotate_left(self, z):
        r = z.right
        z.right = r.left
        if r.left != Nil:
            r.left.parent = z
        r.parent = z.parent
        if z.parent == Nil:
            self.root = r
        elif z == z.parent.left:
            z.parent.left = r
        else:
            z.parent.right = r
        r.left = z
        z.parent = r

    def rotate_right(self, z):
        L = z.left
        z.left = L.right
        if L.right != Nil:
            L.right.parent = z
        L.parent = z.parent
        if z.parent == Nil:
            self.root = L
        elif z == z.parent.left:
            z.parent.left = L
        else:
            z.parent.right = L
        L.right = z
        z.parent = L

if __name__ == '__main__':
    values = [10,3,23,30,13,20,24,26,11,15,8,18,16,7,2,1,19,14,17,12,21,28,25,4,29,22,5,27,6,9]
    tree = RBTree()
    for val in values:
        tree.insert(val, val+100)
        print(f'find {val}: {tree.find(val)}')


