# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.isBST(sequence)

    def isBST(self,sequence):
        if not sequence:
            return True
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for item in sequence[i:-1]:
            if item < root:
                return False
        return self.isBST(sequence[:i]) and self.isBST(sequence[i:-1])




                


if __name__ == '__main__':
    sol = Solution()
    print(sol.VerifySquenceOfBST([4,6,7,5]))