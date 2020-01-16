class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        slow = head
        fast = head
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        # write code here


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    sol = Solution()
    print(sol.FindKthToTail(node1,5).val)