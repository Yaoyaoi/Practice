class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not (pRoot1 and pRoot2):
            return False
        if pRoot1.val == pRoot2.val:
            if self.IsMatch(pRoot1, pRoot2):
                return True
        if self.HasSubtree(pRoot1.left, pRoot2):
            return True
        if self.HasSubtree(pRoot1.right, pRoot2):
            return True
        return False

        
    def IsMatch(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        left = self.IsMatch(pRoot1.left, pRoot2.left)
        right = self.IsMatch(pRoot1.right, pRoot2.right)
        return (left and right)


if __name__ == '__main__':
#    tree1 = None
#    tree2 = None
    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node6 = TreeNode(10)
    node8 = TreeNode(3)
    node9 = TreeNode(5)
    node10 = TreeNode(3)
    node11 = TreeNode(5)

    tree1.left = node1            #  tree 1            
    tree1.right = node2           #---------1
    node1.left = node3            #-----3------7
    node1.right = node4           #---1---5--9---10
    node2.left = node5            #-3---5
    node2.right = node6           
    node3.left = node8            
    node3.right = node9           
                                  # tree 2
    tree2.left = node10           #-----1
    tree2.right = node11          #---3---5 


    sol = Solution()
    print(sol.HasSubtree(tree1, tree2))