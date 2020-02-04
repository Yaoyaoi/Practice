class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = self.FindPathRecursive(root,expectNumber)

        if not result:
            return result

        for i in range(1,len(result)):
            for j in range(len(result)-i):
                if len(result[j]) < len(result[j+1]):
                    temp = result[j]
                    result[j] = result[j+1]
                    result[j+1] = temp
        return result

    def FindPathRecursive(self, root, expectNumber):
        if not root:
            return []
        if root.left == None and root.right == None:
            if root.val == expectNumber:
                return[[root.val]]
            else:
                return []
        result = []
        resultleft = []
        resultright = []
        if root.left:
            resultleft = self.FindPathRecursive(root.left,expectNumber-root.val)
        if root.right:
            resultright = self.FindPathRecursive(root.right,expectNumber-root.val)
        if resultleft:
            for i in range(len(resultleft)):
                resultleft[i].insert(0,root.val)
            result.extend(resultleft)
        if resultright:
            for i in range(len(resultright)):
                resultright[i].insert(0,root.val)
            result.extend(resultright)
        if not result:
            result = []
        return result
        # write code here




if __name__ == '__main__':
    
    tree = TreeNode(1)
    node1 = TreeNode(9)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(6)
    node5 = TreeNode(4)
    node6 = TreeNode(5)

    tree.left = node1            #  tree 1            
    tree.right = node2           #---------1
    node2.left = node3            #-----9------3
    node2.right = node4           #----------2---6
    node3.left = node5            #--------4--5
    node3.right = node6      

    sol = Solution()
    result = sol.FindPath(tree,10)
    print(result)
