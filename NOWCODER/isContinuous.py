class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        minV = None
        maxV = None
        zeroCount = 0
        for item in numbers:
            if item == 0:
                zeroCount += 1
                continue
            if minV == None or minV > item:
                minV = item
            if maxV == None or maxV < item:
                maxV = item
        if maxV - minV <= 4 and maxV - minV >= 4 - zeroCount:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.IsContinuous([1,3,2,5,4]))