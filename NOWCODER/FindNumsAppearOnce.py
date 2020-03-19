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

    def FindNumsAppearOnce(self, array):
        if len(array) <= 2:
            return array
        temp = 0
        for item in array:
            temp = temp^item
        i = 0
        while True:
            if temp&1 == 1:
                break
            temp = temp >> 1
            i += 1
        temp = 1
        while i:
            temp = temp << 1
            i -= 1
        num1 = 0
        num2 = 0
        for item in array:
            if item & temp == temp:
                num1 = num1^item
            else:
                num2 = num2^item
        return [num1,num2]

            
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.FindNumsAppearOnce([1,1,3,2,4,3,5,5]))