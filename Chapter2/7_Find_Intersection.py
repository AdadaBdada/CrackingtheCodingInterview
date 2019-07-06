class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def findIntersection(headA, headB):
    lenA = lenB = 0
    curA, curB = headA, headB

    # calculate the length of two linked list
    while curA:
        lenA += 1
        curA = curA.next

    while curB:
        lenB += 1
        curB = curB.next

    curA = preA = headA
    curB = preB = headB

    # make sure they are start at the same reference to the end
    if lenA > lenB:
        for i in range(lenA - lenB):
            preA = curA
            curA = curA.next

    elif lenA < lenB:
        for i in range(lenB - lenA):
            preB = curB
            curB = curB.next

    while curA:

        if curA == curB and preA == preB:
            return preA
        if preB != preA and curA == curB:
            return curB

        preB = curB
        curB = curB.next
        preA = curA
        curA = curA.next

    return None


if __name__ == "__main__":

    headA = ListNode(4)
    b = ListNode(1)
    c = ListNode(8)
    d = ListNode(4)
    e = ListNode(5)

    headB = ListNode(5)
    x = ListNode(0)
    y = ListNode(1)

    headA.next = b
    b.next = c
    c.next = d
    d.next = e

    headB.next = x
    x.next = y
    y.next = c
    c.next = d
    d.next = e

    print(findIntersection(headA, headB))
