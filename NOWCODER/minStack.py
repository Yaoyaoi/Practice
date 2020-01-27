# -*- coding:utf-8 -*-
class Solution:
#    def __init__(self):
#        self.stack = []
#        self.minlist = []
#
#    def push(self, node):
#        self.stack.append(node)
#        self.minlist = self.insert(self.minlist, node)
#
#    def pop(self):
#        if not self.stack:
#            return None
#        self.minlist.remove(self.top())
#        return self.stack.pop()
#
#    def top(self):
#        if not self.stack:
#            return None
#        return self.stack[len(self.stack)-1]
#        # write code here
#
#    def min(self):
#        if not self.minlist:
#            return None
#        return self.minlist[0]
#        # write code here
#
#    def insert(self, array, node):
#        array.append(node)
#        i = len(array) - 1
#        while i:
#            if array[i-1] > array[i]:
#                temp = array[i]
#                array[i] = array[i-1]
#                array[i-1] = temp
#            else:
#                break
#            i -= 1
#        return array

#    def __init__(self):
#        self.stack = []
#        self.minStack = []
#
#    def push(self, node):
#        self.stack.append(node)
#        if not self.minStack:
#            self.minStack.append(node)
#        elif node <= self.minStack[len(self.minStack)-1]:
#            self.minStack.append(node)
#
#    def pop(self):
#        if not self.stack:
#            return None
#        elif self.top() == self.minStack[len(self.minStack)-1]:
#            self.minStack.pop()
#        return self.stack.pop()
#
#    def top(self):
#        if not self.stack:
#            return None
#        return self.stack[len(self.stack)-1]
#        # write code here
#
#    def min(self):
#        if not self.minStack:
#            return None
#        return self.minStack[len(self.minStack)-1]
#        # write code here

    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, node):
        if not self.minValue:
            self.minValue = node
            self.stack.append(0)
            return
        self.stack.append(node - self.minValue)
        if node < self.minValue:
            self.minValue = node

    def pop(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        if node < 0:
            self.minValue = self.minValue - node
        return self.minValue + node

    def top(self):
        if not self.stack:
            return None
        top = self.stack[len(self.stack)-1]
        if top < 0:
            return self.minValue
        return self.minValue + top
        # write code here

    def min(self):
        return self.minValue

if  __name__ == '__main__':
    sol = Solution()
    sol.push(2)
    sol.push(1)
    sol.push(1)
    sol.push(0)
    print(sol.min())
    sol.pop()
    print(sol.min())
    sol.pop()
    print(sol.min())
    sol.pop()
    print(sol.min())


#    array = sol.insert([], 1)
#    print(array)
#    array = sol.insert(array,8)
#    print(array)
#    array = sol.insert(array,3)
#    print(array)
#    array = sol.insert(array,0)
#    print(array)