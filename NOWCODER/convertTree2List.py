class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        minNode, maxNode = self.traverseTree(None, pRootOfTree, None)
        return minNode

    #def traverseTree(self, before, node, after):
    #    # before/after: 父节点 （如果父节点大 after = parent before = None
    #    # minNode:以node为根节点的子树的最小节点
    #    # maxNode:以node为根节点的子树的最大节点
    #    minNode = maxNode = node
    #    
    #    # 如果有左子树
    #    if node.left:
    #        #获得左子树的最大最小节点
    #        lMin, lMax  = self.traverseTree(before, node.left, node)
    #        #该节点的前一个节点是左子树的最大节点
    #        #该树的最小节点是左子树的最小节点
    #        before = lMax
    #        minNode = lMin
    #    # 如果有右子树
    #    if node.right:
    #        # 获得右子树的最大最小节点
    #        rMin, rMax = self.traverseTree(node, node.right, after)
    #        #该节点的后一个节点是右子树的最小节点
    #        #该树的最大节点是右子树的最大节点
    #        after = rMin
    #        maxNode = rMax
    #    node.left = before
    #    node.right = after
    #    return (minNode, maxNode)

    def printList(self, pHead):
        array = []
        while pHead:
            array.append(pHead.val)
            pHead = pHead.right
        return array

if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(9)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(10)
    node8 = TreeNode(1)
    node9 = TreeNode(6)
    node10 = TreeNode(8)

    node1.left = node2            #  tree             
    node1.right = node3           #---------5
    node2.left = node4            #-----3------9
    node2.right = node5           #---2---4--7---10
    node3.left = node6            #-1-------6-8
    node3.right = node7           
    node4.left = node8            
    node6.left = node9    
    node6.right = node10

    sol = Solution()
    treeList = sol.Convert(node1)
    print(sol.printList(treeList))