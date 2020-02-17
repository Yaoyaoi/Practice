class Solution:
    #def FindGreatestSumOfSubArray(self, array):
    #    if not array:
    #        return 0
    #    tempSum = array[0]
    #    maxSum = tempSum
    #    for item in array[1:]:
    #        if tempSum < 0:
    #                tempSum = item
    #        else:
    #            tempSum += item
    #        if tempSum > maxSum:
    #            maxSum = tempSum
    #    return maxSum
    # 简化写法
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        maxSum = array[0]
        for i in range(1,len(array)):
            array[i] += array[i - 1] if array[i - 1] > 0 else 0
            maxSum = array[i] if array[i] > maxSum else maxSum
        return maxSum

if __name__ == "__main__":
    sol = Solution()
    print(sol.FindGreatestSumOfSubArray([-1,-3,-4,-5,-2]))