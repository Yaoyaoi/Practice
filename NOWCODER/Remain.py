class LinkListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    #def LastRemaining_Solution(self, n, m):
    #    if not n or not m:
    #        return -1
    #    node = head = LinkListNode(-1)
    #    for i in range(n):
    #        nodei = LinkListNode(i)
    #        node.next = nodei
    #        node = nodei
    #    node.next = head.next
    #    lastNode = node
    #    node = node.next
    #    while node.next:
    #        i = 0
    #        while i != m - 1:
    #            i += 1
    #            lastNode = node
    #            node = node.next
    #        i = 0
    #        lastNode.next = node.next
    #        node = node.next
    #        if lastNode.val == node.val:
    #            node.next = None
    #    return node.val
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last+m)%i
        return last


if __name__ == "__main__":
    sol = Solution()
    print(sol.LastRemaining_Solution(10,3))