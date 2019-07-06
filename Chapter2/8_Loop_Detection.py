# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def loopDetection(head):

    fast = slow = head
    start = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        # collision
        if slow == fast:

            # move slow to head, keep fast at meeting point. K steps from the loop start
            # if they move at the same pace, they must meet at loop start
            slow = head

            # edge case [1,2] and 2.next = 1
            if start == fast:
                return start

            while fast:
                slow = slow.next
                fast = fast.next

                if slow == fast:
                    return slow
    return None


if __name__ == "__main__":

    a = ListNode('A')
    b = ListNode('B')
    c = ListNode('C')
    d = ListNode('D')
    e = ListNode('E')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c

    res = loopDetection(a)
    print(res.val)
