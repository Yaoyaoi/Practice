class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #方法二：
    def __init__(self):
        self.result = []
        self.tempList = []
        self.sum = 0
        self.expNum = None
    
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        self.expNum = expectNumber
        self.TraverseTree(root)

        # 排序

        for i in range(1,len(self.result)):
            for j in range(len(self.result)-i):
                if len(self.result[j]) < len(self.result[j+1]):
                    temp = self.result[j]
                    self.result[j] = self.result[j+1]
                    self.result[j+1] = temp

        return self.result

    # 遍历树的路径（递归
    #def TraverseTree(self, root):
    #    if not root:
    #        return []
    #    self.sum += root.val
    #    self.tempList.append(root.val)
    #    if self.sum == self.expNum and root.left == None and root.right == None:
    #        self.result.append(self.tempList[:])
    #    else:
    #        if root.left:
    #            self.TraverseTree(root.left)
    #        if root.right:
    #            self.TraverseTree(root.right)
    #        
    #    self.sum -= root.val
    #    self.tempList.pop()

    遍历树的路径（非递归：栈
    def TraverseTree(self, root):
        if not root:
            return []
        stack = [(root,[root.val],root.val)]
        while stack:
            node, path, sumPath = stack.pop()
            if sumPath == self.expNum and node.left == None and node.right == None:
                self.result.append(path)
            else:
                if node.left:
                    stack.append((node.left, path + [node.left.val], sumPath+node.left.val))
                if node.right:
                    stack.append((node.right, path + [node.right.val], sumPath+node.right.val))


    
    
    
    # 方法一：
    #def FindPath(self, root, expectNumber):
    #    if not root:
    #        return []
    #    result = self.FindPathRecursive(root,expectNumber)

    #    if not result:
    #        return result
    
    #    for i in range(1,len(result)):
    #        for j in range(len(result)-i):
    #            if len(result[j]) < len(result[j+1]):
    #                temp = result[j]
    #                result[j] = result[j+1]
    #                result[j+1] = temp
    #    return result

    #def FindPathRecursive(self, root, expectNumber):
    #    if not root:
    #        return []
    #    if root.left == None and root.right == None:
    #        if root.val == expectNumber:
    #            return[[root.val]]
    #        else:
    #            return []
    #    result = []
    #    resultleft = []
    #    resultright = []
    #    if root.left:
    #        resultleft = self.FindPathRecursive(root.left,expectNumber-root.val)
    #    if root.right:
    #        resultright = self.FindPathRecursive(root.right,expectNumber-root.val)
    #    if resultleft:
    #        for i in range(len(resultleft)):
    #            resultleft[i].insert(0,root.val)
    #        result.extend(resultleft)
    #    if resultright:
    #        for i in range(len(resultright)):
    #            resultright[i].insert(0,root.val)
    #        result.extend(resultright)
    #    if not result:
    #        result = []
    #    return result
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
