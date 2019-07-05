class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def sumLists(l1, l2):

    l = l_head = ListNode(0)

    l1_ = ''
    l2_ = ''

    while l1:
        l1_ += str(l1.val)
        l1 = l1.next

    while l2:
        l2_ += str(l2.val)
        l2 = l2.next

    l1_ = int(l1_[::-1])
    l2_ = int(l2_[::-1])

    sum_val = str(l1_+l2_)

    while sum_val != '':

        l.next = ListNode(int(sum_val[-1]))
        l = l.next
        sum_val = sum_val[:-1]

    l.next = None

    return l_head.next


def sumLists_2(l1, l2):
    '''
    careful to handle the condition when one linked list is shorter than another
    mimic the process recrusively by adding node by node

    carry is used to carry over any 'excess' data to the next node
    8 + 9 = 17
    carry = 1

    '''

    carry = 0
    res = res_head = ListNode(0)

    while l1 or l2 or carry:

        value = carry
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next

        res.next = ListNode(value % 10)
        carry = value // 10
        res = res.next

    return res_head.next


if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)

    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)

    a.next = b
    b.next = c

    d.next = e
    e.next = f

    z = ListNode(5)
    k = ListNode(5)

    res = sumLists_2(z, k)
    print(res.val)
    print(res.next.val)
