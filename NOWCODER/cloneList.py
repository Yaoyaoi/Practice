class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    #def Clone(self, pHead):
    #    pHeadC = head = RandomListNode(0)
    #    # copy list
    #    while pHead:
    #        node = RandomListNode(pHead.label)
    #        node.random = pHead.random
    #        head.next = node
    #        pHead.random = node
    #        head = head.next
    #        pHead = pHead.next
    #    
    #    # copy the random pointer
    #    head = pHeadC.next
    #    while head:
    #        if head.random:
    #            head.random = head.random.random
    #        head = head.next
    #    return pHeadC.next

    def Clone(self, pHead):
        if not pHead:
            return pHead
        #copy nodes
        headM = pHead
        while headM:
            node = RandomListNode(headM.label)
            node.next = headM.next
            headM.next = node
            headM = node.next

        # copy randoms 
        headM = pHead
        while headM:
            if headM.random:
                headM.next.random = headM.random.next
            headM = headM.next.next

        #split
        headM = pHead
        headMC = pHeadC = pHead.next
        while headM:
            headM.next = headMC.next
            if headMC.next:
                headMC.next = headMC.next.next
            headM = headM.next
            headMC = headMC.next
        return pHeadC


    def printRandomNodeLabel(self, pHead):
        printList = []
        while pHead:
            if pHead.random:
                printList.append(pHead.random.label)
            else:
                printList.append(pHead.random)
            pHead = pHead.next
        return printList

if __name__ == '__main__':
    head = RandomListNode(0)
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node5 = RandomListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head.random = node2
    node1.random = head
    node2.random = node3
    node3.random = node5
    node4.random = node1
    node5.random = node4

    sol = Solution()
    print(sol.printRandomNodeLabel(head))
    headC = sol.Clone(head)
    print(sol.printRandomNodeLabel(headC))
