class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root:
            left = root.left
            root.left = self.Mirror(root.right)
            root.right = self.Mirror(left)
        return root
        # write code he re

    def postPrintBinaryTree(self,Head):
        if not Head:
            return None
        post = []
        if Head.left:
            post.extend(self.postPrintBinaryTree(Head.left))
        if Head.right:
            post.extend(self.postPrintBinaryTree(Head.right))
        post.append(Head.val)
        return post

if __name__ == '__main__':

    tree = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node6 = TreeNode(10)
    node8 = TreeNode(3)
    node9 = TreeNode(5)

    tree.left = node1             #  tree 1            
    tree.right = node2            #          1
    node1.left = node3            #       /   \
    node1.right = node4           #     3      7
    node2.left = node5            #    / \    / \
    node2.right = node6           #   1   5  9   10
    node3.left = node8            #  / \
    node3.right = node9           # 3   5



    sol = Solution()
    mirrorTree = sol.Mirror(tree)
    print(sol.postPrintBinaryTree(mirrorTree))
    