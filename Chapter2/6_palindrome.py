class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    '''
    Palindrome: Implement a function to check if a linked list is a palindrome.

    be careful to handle the case where the length of the linked list is odd
    '''
    fast = slow = head
    res = []  # stack

    while fast and fast.next:
        res.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    # handle the length linked list is odd
    if fast:
        slow = slow.next

    while slow:
        if res.pop() != slow.val:
            return False
        slow = slow.next

    return res == []


if __name__ == "__main__":

    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(3)
    e = ListNode(1)
    f = ListNode(2)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(isPalindrome(a))
