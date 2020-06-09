class ListNode:

    def __init__(self, value = None, *, val = None, prev = None, next = None):
        if value is None:
            value = val
        self.value = value
        self.prev = prev
        self.next = next

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, v):
        self.value = v

class LinkList:

    @classmethod
    def new_s(cls, *args, **kwargs):
        return new_slist(*args, **kwargs)

    @classmethod
    def show(cls, L):
        print_list(L)

LinkedList = LinkList

def print_list(L):
    p = L
    print('LinkedList[', end = '')
    while p:
        if p.next:
            print(p.value, end = ', ')
        else:
            print(p.value, end = '')
        p = p.next
    print(']')

def new_slist(values, *, with_head = False, cls = ListNode, builder = None):
    if not builder:
        builder = lambda c, v: c(v)

    if with_head:
        h = builder(cls, None)
        h.next = new_slist(values, cls = cls, builder = builder)
        return h

    h = p = None
    for v in values:
        n = builder(cls, v)
        if not p:
            h = p = n
        else:
            p.next = n
            p = n
    return h

def new_slist_h(values, *, cls = ListNode, builder = None):
    return new_slist(values, cls = cls, builder = builder)

def new_dlist(values, with_head = False):
    if with_head:
        return new_dlist_h(values)
    h = p = None
    for v in values:
        n = ListNode(v)
        if not p:
            h = p = n
        else:
            p.next = n
            n.prev = p
            p = n
    return h

def new_dlist_h(values):
    h = ListNode()
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

