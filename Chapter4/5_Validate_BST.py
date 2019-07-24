# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    '''
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(N)
    '''

    stack = []

    def inorder(node):

        if not node:
            return

        inorder(node.left)
        stack.append(node.val)
        inorder(node.right)

    inorder(root)

    for i in range(1, len(stack)):

        if stack[i-1] >= stack[i]:
            return False

    return True


def isValidBST_Recursion(root: TreeNode) -> bool:
    '''
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(N)
    '''

    def helper(node, min=float('-inf'), max=float('inf')):

        if not node:
            return True

        val = node.val

        if not min < node.val < max:
            return False

        return helper(node.left, min, val) and helper(node.right, val, max)

    return helper(root)


def isValidBST_Iteration(root: TreeNode) -> bool:
    '''
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(N)
    '''

    if not root:
        return True

    stack = [(root, float('-inf'), float('inf'))]

    while stack:

        root, lower, upper = stack.pop()

        if not root:
            continue

        if root.val <= lower or root.val >= upper:
            return False

        stack.append((root.right, root.val, upper))
        stack.append((root.left, lower, root.val))

    return True
