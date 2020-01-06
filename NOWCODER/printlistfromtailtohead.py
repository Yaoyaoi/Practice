class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ArrayList = []
        if not listNode:
            return ArrayList
        while listNode:
            ArrayList.append(listNode.val)
            listNode = listNode.next
        ArrayList.reverse()
        return ArrayList
    
    def solution1(self, listNode): # 栈
        ArrayList = []
        temp = []
        if not listNode:
            return ArrayList
        while listNode:
            temp.append(listNode.val)
            listNode = listNode.next
        while temp:
            ArrayList.append(temp.pop())
        return ArrayList

    def solution2(self, listNode):  # 递归
        ArrayList = []
        if listNode:
            ArrayList.extend(self.solution2(listNode.next))
            ArrayList.append(listNode.val)
        return ArrayList

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3


    solution = Solution()
    print(solution.solution2(node1))