class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def remove_dups(head):

    if head == None:
        return

    current = head
    seen = set([current.val])

    while current.next:

        if current.next.val in seen:
            current.next = current.next.next

        else:
            seen.add(current.next.val)
            current = current.next

    return head


def remove_dups_followup(head):
    '''
    current pointer: iterates through the linked list
    runner  pointer: checks all subsequent nodes for duplicates
    '''

    if head == None:
        return

    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    return head


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

    # check remove_dups
    res = remove_dups(a)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)

    # check remove_dups_followup
    res = remove_dups_followup(a)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
