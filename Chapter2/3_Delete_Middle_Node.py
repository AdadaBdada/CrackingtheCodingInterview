class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


'''
   Note that this problem cannot be solved if the node to be deleted is the last
   node in the linked list. That's okay - your interviewer wants you to point that
   out, and to discuss how to handle this case. You could, for example, consider
   marking the node as dummy.

'''
