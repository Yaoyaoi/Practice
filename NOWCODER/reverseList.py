
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return pHead
        temp = []
        while pHead:
            temp.append(pHead)
            pHead = pHead.next
        Head = listNode = temp.pop()
        while temp:
            listNode.next = temp.pop()
            listNode = listNode.next
        listNode.next = None
        return Head


    def ReverseList2(self, pHead):
        prep = None
        nextp = None
        while pHead:
            nextp = pHead.next
            pHead.next = prep
            prep = pHead
            pHead = nextp
        return prep
        


    def PrintList(self, Head):
        while Head:
            print(Head.val)
            Head = Head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3


    solution = Solution()
    solution.PrintList(solution.ReverseList2(node1))