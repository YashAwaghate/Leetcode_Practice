# Question is to get sum of left leaves in binary tree:

class TreeNode:
    def __init__(self,a):
        self.val = a
        self.left = self.right = None

    def sumOfLeftLeaves(root):
        def dfs(node):
            if not node:
                return 0
            total = 0
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val
            total += dfs(node.left)
            total += dfs(node.right)
            return total

        return dfs(root)


# Main function to test the TreeNode class
def main():
    # Create nodes
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Calculate sum of left leaves
    result = TreeNode.sumOfLeftLeaves(root)
    print("Sum of left leaves:", result)

if __name__ == "__main__":
    main()