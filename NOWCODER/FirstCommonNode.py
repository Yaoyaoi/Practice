class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        current = pHead1
        pLast1 = None
        count1 = 0
        while current:
            count1 += 1
            pLast1 = current
            current = current.next
        current = pHead2
        pLast = None
        count2 = 0
        while current:
            count2 += 1
            pNext = current.next
            current.next = pLast
            pLast = current
            current = pNext
        current = pHead1
        count3 = 0
        pLast2 = None
        while current:
            count3 +=1
            pLast2 = current
            current = current.next
        if pLast1 == pLast2:
            return None
        diff = (count1 + count2 - count3 + 1)//2
        current = pLast
        pLast = None
        result = None
        while current:
            diff -= 1
            if not diff and result == None:
                result = current
            pNext = current.next
            current.next = pLast
            pLast = current
            current = pNext
        return result

if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    
    node1.next = node2
    node2.next = node3
    node3.next = node6

    node4.next = node5
    node5.next = node6

    node6.next = node7
    node = sol.FindFirstCommonNode(node1, node4) 
    while node:
        print(node.val)
        node = node.next