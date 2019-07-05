class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):

    before = before_head = ListNode(0)
    after = after_head = ListNode(0)

    while head:

        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

        after.next = None
        before.next = after_head.next

    return before_head.next


if __name__ == "__main__":
    # ListNode
    a = ListNode(3)
    b = ListNode(5)
    c = ListNode(8)
    d = ListNode(5)
    e = ListNode(10)
    f = ListNode(2)
    g = ListNode(1)

    # link ListNode
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    res = partition(a, 5)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
    print(res.next.next.next.val)
    print(res.next.next.next.next.val)
    print(res.next.next.next.next.next.val)
    print(res.next.next.next.next.next.next.val)
