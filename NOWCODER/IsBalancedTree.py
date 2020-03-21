class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return False
        result, height = self.__isBalanced(pRoot)
        return result

    def __isBalanced(self, pRoot):
        resultL = resultR = True
        heightL = heightR = 0
        if pRoot.left:
            if pRoot.left.val > pRoot.val:
                return False, 0
            resultL, heightL = self.__isBalanced(pRoot.left)
        if pRoot.right:
            if pRoot.right.val < pRoot.val:
                return False, 0
            resultR, heightR = self.__isBalanced(pRoot.right)
        heightDiff = heightR-heightL if heightR > heightL else heightL - heightR
        return resultL and resultR and heightDiff < 2, max(heightL,heightR)+1

if __name__ == "__main__":
    tree1 = TreeNode(5)
    node11 = TreeNode(3)
    node12 = TreeNode(6)
    node13 = TreeNode(1)
    node14 = TreeNode(4)
    node15 = TreeNode(7)
    tree1.left = node11
    tree1.right = node12
    node11.left = node13
    node11.right = node14
    node12.right = node15

    tree2 = TreeNode(5)
    node21 = TreeNode(2)
    tree2.right = node21

    tree3 = TreeNode(5)
    node31 = TreeNode(1)
    node32 = TreeNode(6)
    node33 = TreeNode(7)
    node34 = TreeNode(8)
    tree3.left = node31
    tree3.right = node32
    node32.right = node33
    node33.right = node34

    sol = Solution()
    print(sol.IsBalanced_Solution(tree1))
    print(sol.IsBalanced_Solution(tree2))
    print(sol.IsBalanced_Solution(tree3))