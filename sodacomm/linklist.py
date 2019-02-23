class Node:

    def __init__(self, value = None, *, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

def print_list(L):
    p = L
    while p:
        print(p.value, end = ' ')
        p = p.next
    print('')

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

def iter_nodes(L):
    p = L
    while p:
        yield p
        p = p.next

def find_first(L, v):
    for p in iter_nodes(L):
        if p.value == v:
            return p

def get_tail(L):
    last = None
    for p in iter_nodes(L):
        last = p
    return last

