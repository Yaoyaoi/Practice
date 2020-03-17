class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        count = 1
        depth = 1
        Stack = [(pRoot, count)]
        while Stack:
            node, count = Stack.pop(0)
            if node.left == None and node.right == None:
                if count > depth:
                    depth = count
            if node.left:
                Stack.append((node.left, count+1))
            if node.right:
                Stack.append((node.right, count+1))
        return depth
    
if __name__ == "__main__":
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
    tree2.right = node11 

    sol = Solution()
    print(sol.TreeDepth(tree1))
    print(sol.TreeDepth(tree2))