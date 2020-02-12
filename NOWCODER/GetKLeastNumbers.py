
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput) or k <= 0:
            return []
        begin = 0
        end = len(tinput)-1
        tempK = self.Partition(tinput, begin, end)
        if tempK > k-1:
            end = tempK-1
        if tempK < k-1:
            begin = tempK+1
        while tempK != k-1:
            tempK = self.Partition(tinput, begin, end)
            if tempK > k-1:
                end = tempK-1
            if tempK < k-1:
                begin = tempK+1
        return sorted(tinput[:k])

    def Partition(self, tinput, begin, end):
        pivot = tinput[begin]
        i = begin
        j = end
        while i < j:
            while i < j and pivot <= tinput[j]:
                j -= 1
            tinput[i] = tinput[j]
            while i < j and pivot >= tinput[i]:
                i += 1
            tinput[j] = tinput[i]
        tinput[i] = pivot
        return i

    #def GetLeastNumbers_Solution(self, tinput, k):
    #    result = []
    #    if not tinput or k > len(tinput) or k == 0:
    #        return result
    #    for i in range(len(tinput)):
    #        if i < k:
    #            self.insertSiftUP(result, tinput[i])
    #        elif tinput[i] < result[0]:
    #            result[0] = tinput[i]
    #            self.siftDown(result, 0)
    #    return sorted(result)
    #
    #def insertSiftUP(self, array, x):
    #    array.append(x)
    #    i = len(array)-1
    #    while i > 0:
    #        parent = (i - 1)//2
    #        if x <= array[parent]:
    #            break
    #        array[i] = array[parent]
    #        i = parent
    #    array[i] = x
    #
    #def siftDown(self, array, nodeIndex):
    #    if nodeIndex*2+1 > len(array):
    #        return
    #    biggest = nodeIndex
    #    if nodeIndex*2+1 < len(array):
    #        if array[nodeIndex*2+1] > array[biggest]:
    #            biggest  = nodeIndex*2+1
    #    if nodeIndex*2+2 < len(array):
    #        if array[nodeIndex*2+2] > array[biggest]:
    #            biggest = nodeIndex*2+2
    #    if nodeIndex != biggest:
    #        array[nodeIndex], array[biggest] = array[biggest], array[nodeIndex]
    #        self.siftDown(array,biggest)


if __name__ == "__main__":
    array = [4,5,1,6,2,7,3,8]
    sol = Solution()
    print(sol.GetLeastNumbers_Solution(array,1))