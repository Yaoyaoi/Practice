class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        i = 0
        j = len(rotateArray)-1
        while(i < j):
            if rotateArray[i] < rotateArray[j]:
                return rotateArray[i]
            mid = (i+j) >> 1
            if rotateArray[i] < rotateArray[mid]:
                i = mid + 1
            elif rotateArray[j] > rotateArray[mid]:
                j = mid
            else:
                i += 1
        return rotateArray[i]


if __name__ == '__main__':
    list = [1,0,1,1,1]
    sol = Solution()
    print(sol.minNumberInRotateArray(list))