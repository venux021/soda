class Node:

    def __init__(self, value = None):
        self.value = value
        self.prev = self.next = None

def new_slist(values):
    h = p = None
    for v in values:
        n = Node(v)
        if not p:
            h = p = n
        else:
            p.next = n
            p = n
    return h

def new_slist_h(values):
    h = Node()
    h.next = new_slist(values)
    return h

def new_dlist(values):
    h = p = None
    for v in values:
        n = Node(v)
        if not p:
            h = p = n
        else:
            p.next = n
            n.prev = p
            p = n
    return h

def new_dlist_h(values):
    h = Node()
    k = new_dlist(values)
    h.next = k
    k.prev = h
    return h
