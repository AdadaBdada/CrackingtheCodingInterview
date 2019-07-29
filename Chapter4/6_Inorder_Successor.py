# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

    ans = None
    while root:
        if p.val < root.val:
            ans = root
            root = root.left
        else:
            root = root.right

    return ans


if __name__ == "__main__":

    root = TreeNode(2)
    root.left, root.right = TreeNode(1), TreeNode(3)
    res = inorderSuccessor(root, p=TreeNode(1))
    print(res.val)
