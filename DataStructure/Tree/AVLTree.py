class AVLNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, root = None):
        if not root:
            self.root = root
        elif type(root) is AVLNode:
            self.root = root
        else:
            rootNode = AVLNode(root)
            self.root = rootNode

    def __LL(self, rootNode):
        nodeA = rootNode
        nodeB = rootNode.left
        nodeA.left = nodeB.right
        nodeB.right = nodeA
        return nodeB

    def __RR(self, rootNode):
        nodeA = rootNode
        nodeB = rootNode.right
        nodeA.right = nodeB.left
        nodeB.left = nodeA
        return nodeB

    def __LR(self, rootNode):
        nodeA = rootNode
        nodeB = rootNode.left
        nodeC = rootNode.left.right
        nodeB.right, nodeA.left = nodeC.left,nodeC.right
        nodeC.left, nodeC.right = nodeB, nodeA
        return nodeC
    
    def __RL(self, rootNode):
        nodeA = rootNode
        nodeB = rootNode.right
        nodeC = rootNode.right.left
        nodeB.left, nodeA.right = nodeC.right, nodeC.left
        nodeC.left, nodeC.right = nodeA, nodeB
        return nodeC

        # 可以插入一个值，也可以插入一个序列 
    def Insert(self, x):
        if type(x) is list:
            root = self.root
            for item in x:
                root = self.__Insert(item, root)
            self.root = root
        else:
            self.root = self.__Insert(item, self.root)

    def __Insert(self, x, root): 
        if not root:
            root = AVLNode(x)
            return root
        if x < root.val:# 插入左子树
            if root.left:
                root.left = self.__Insert(x, root.left)
                heightLeft = self.Height(root.left)
                heightRight = self.Height(root.right)
                if heightLeft - heightRight == 2:
                    if x < root.left.val:
                        root = self.__LL(root)
                    else:
                        root = self.__LR(root)
            else:
                root.left = AVLNode(x)
        elif x > root.val:#插入右子树
            if root.right:
                root.right = self.__Insert(x, root.right)
                heightLeft = self.Height(root.left)
                heightRight = self.Height(root.right)
                if heightRight - heightLeft == 2:
                    if x > root.right.val:
                        root = self.__RR(root)
                    else:
                        root = self.__RL(root)
            else:
                root.right = AVLNode(x)
        return root

    def Height(self, root):
        if not root:
            return 0
        heightLeft = self.Height(root.left)
        heightRight = self.Height(root.right)
        return max(heightLeft,heightRight)+1


if __name__ == "__main__":
    myAVLTree = AVLTree()
    myAVLTree.Insert([1,3,5,6,4,3.5,3.7])
    