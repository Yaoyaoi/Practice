class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        Head = TreeNode(pre[0])
        if len(pre) < 2:
            return Head
        index = tin.index(pre[0])
        Head.left = self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        Head.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return Head


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
            


if __name__ == "__main__":
    preList = [1,2,4,7,3,5,6,8]
    tinList = [4,7,2,1,5,3,8,6]
    solution = Solution()
    print(solution.postPrintBinaryTree(solution.reConstructBinaryTree(preList,tinList)))