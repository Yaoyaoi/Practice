class Solution:
    #def __init__(self):
    #    self.stack = []
    #    
    #def IsPopOrder(self, pushV, popV):
    #    i = 0
    #    j = -1
    #    while i < len(pushV):
    #        if not self.stack or self.top() != popV[i]: 
    #            j += 1
    #            while j < len(pushV) and pushV[j] != popV[i]:
    #                self.stack.append(pushV[j])
    #                j += 1
    #            if j == len(pushV):
    #                return False
    #        elif self.stack:
    #            self.stack.pop()
    #        i += 1
    #    return True

    #def top(self):
    #    if not self.stack:
    #        return None
    #    return self.stack[len(self.stack)-1]
    #    # write code here

    def IsPopOrder(self, pushV, popV):
        stack = []
        i = 0
        for item in pushV:
            stack.append(item)
            while stack and stack[len(stack)-1] == popV[i]:
                stack.pop()
                i += 1
        return False if stack else True



if __name__ == '__main__':
    sol = Solution()
    print(sol.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
    print(sol.IsPopOrder([1,2,3,4,5],[5,4,1,2,3]))