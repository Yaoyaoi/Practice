class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, node):
        while self.list2:
            self.list1.append(self.list2.pop())
        self.list2.append(node)
        while self.list1:
            self.list2.append(self.list1.pop())
        # write code here


    def pop(self):
        if self.list2:
            return self.list2.pop()
        # return xx


if __name__ == "__main__":
    sol = Solution()
    sol.push(1)
    sol.push(4)
    sol.push(6)
    print(sol.pop())
    print(sol.pop())
    sol.push(7)
    print(sol.pop())