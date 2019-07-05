class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def kth_to_last(head, k):
    '''
    take O(n) time and O(1) space
    '''

    right = head
    left = head

    for i in range(k):

        if not right.next:
            raise LookupError('Error: n is larger than the linked list.')

        right = right.next

    while right:

        right = right.next
        left = left.next

    return left


if __name__ == "__main__":
    # ListNode
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(2)

    # link ListNode
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    left = kth_to_last(a, 2)
    print(left.val)
    print(left.next.val)
