# 102. Binary Tree Level Order Traversal


from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Approach 1: Recursion
# Time complexity : O(N) since each node is processed exactly once.
# Space complexity: O(N) to keep the output structure which contains N node values.


def levelOrder(root):

    levels = []

    if not root:
        return levels

    def helper(node, level):

        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels


# Approach 2: Iteration


def levelOrder_2(root):
    '''
    BFS solution
    While queue is not empty :
        - Start the current level by adding an empty list into output structure levels.
        - Compute how many elements should be on the current level : it's a queue length.
        - Pop out all these elements from the queue and add them into the current level.
        - Push their child nodes into the queue for the next level.
        - Go to the next level level++.
    '''
    levels = []

    level = 0
    queue = deque([root])

    while queue:
        levels.append([])
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return levels


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    res = levelOrder_2(root)
    print(res)
