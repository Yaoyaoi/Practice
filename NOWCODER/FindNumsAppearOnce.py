class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    # 方法一： hashmap
    #def FindNumsAppearOnce(self, array):
    #    minV = min(array)
    #    maxV = max(array)
    #    hashTable = [0] * (maxV-minV+1)
    #    for item in array:
    #        hashTable[item-minV] += 1
    #    result = []
    #    for i in range(len(hashTable)):
    #        if hashTable[i] == 1:
    #            result.append(i+minV)
    #    return result


        

if __name__ == "__main__":
    sol = Solution()
    print(sol.FindNumsAppearOnce([1,1,3,2,4,3,5,5]))