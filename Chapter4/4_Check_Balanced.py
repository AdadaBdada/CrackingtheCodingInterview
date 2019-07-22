class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    '''
    why -1: For leaf node, heights will be 0. the node == none, getHeights(node.left) = -1
            getHeights(node.right) = -1, max(-1,-1) + 1 = 0 which is the heights of leaf node.


    Time complexity: O(NlogN)
                    since each node is 'touched' once per node above it
    '''

    def isBalalanced(self, root: TreeNode) -> bool:

        if root == None:
            return True

        def getHeights(node):

            if node == None:
                return -1
            else:
                return max(getHeights(node.left), getHeights(node.right)) + 1

        diffHeights = getHeights(root.right) - getHeights(root.left)

        if abs(diffHeights) > 1:
            return False
        else:
            return self.isBalalanced(root.right) and self.isBalalanced(root.left)


class Solution_Optimal:

    '''
    This improved algorithm works by checking the height of each subtrees as we recurse
    down from the root. If heghtDiff > 1 then return -1, we will immediately break
    and return an error code which is -1 from the current call.

    '''

    def isBalanced(self, root: TreeNode) -> bool:

        return self.checkHeights(root) != -1

    def checkHeights(self, root: TreeNode) -> int:

        if root == None:
            return 0

        leftHeight = self.checkHeights(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.checkHeights(root.right)
        if rightHeight == -1:
            return -1

        heghtDiff = leftHeight - rightHeight
        if abs(heghtDiff) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1


if __name__ == "__main__":

    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.left.left = None
    head.left.right = None
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)

    solution = Solution_Optimal()

    print(solution.isBalanced(head))
