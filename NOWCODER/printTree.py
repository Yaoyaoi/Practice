# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #def __init__(self):
    #    self.treeList = []
    ## 返回从上到下每个节点值列表，例：[1,2,3]
    #def PrintFromTopToBottom(self, root):
    #    if root:
    #        self.treeList.append(root.val)
    #        nextlist = [root]
    #        self.getNextList(nextlist)
    #    return self.treeList
    #    # write code here

    #def getNextList(self, lastlist):
    #    nextlist = []
    #    for item in lastlist:
    #        if item.left:
    #            nextlist.append(item.left)
    #            self.treeList.append(item.left.val)
    #        if item.right:
    #            nextlist.append(item.right)
    #            self.treeList.append(item.right.val)
    #    if nextlist:
    #        self.getNextList(nextlist)
    def PrintFromTopToBottom(self, root):
        treeList = []
        if not root:
            return treeList
        queue = [root]
        while queue:
            node = queue.pop(0)
            treeList.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return treeList
        

if __name__ ==  '__main__':
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
    print(sol.PrintFromTopToBottom(tree1))
    print(sol.PrintFromTopToBottom(tree2))