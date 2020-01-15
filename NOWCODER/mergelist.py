class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        pHead3 = result = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pHead3.next = pHead1
                pHead3 = pHead3.next
                pHead1 = pHead1.next
            else:
                pHead3.next = pHead2
                pHead3 = pHead3.next
                pHead2 = pHead2.next
        pHead3.next = None
        if pHead1:
            pHead3.next = pHead1
        if pHead2:
            pHead3.next = pHead2
        return result.next
    
    def Merge1(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val < pHead2.val:
            result = pHead1
            result.next = self.Merge1(pHead1.next, pHead2)
        else:
            result = pHead2
            result.next = self.Merge1(pHead1, pHead2.next)
        return result

    def printList(self, pHead):
        l = []
        while pHead:
            l.append(pHead.val)
            pHead = pHead.next
        print(l)



if __name__ == "__main__":
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)
    Node5 = ListNode(5)
    Node6 = ListNode(6)
    Node7 = ListNode(7)
    Node8 = ListNode(8)

    List1 = Node1
    Node1.next = Node3
    Node3.next = Node5
    
    List2 = Node2
    Node2.next = Node4
    Node4.next = Node6
    Node6.next = Node7
    Node7.next = Node8

    sol = Solution()
    sol.printList(List1)
    sol.printList(List2)  
    sol.printList(sol.Merge1(List1, List2))  