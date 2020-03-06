# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        dataSorted, count = self.MergeSort(data)
        return count%1000000007
    
    def MergeSort(self, data):
        count = 0
        if len(data) < 2:
            return data,0
        mid = len(data)//2
        leftD, count1 = self.MergeSort(data[:mid])
        rightD, count2 = self.MergeSort(data[mid:])
        count += count1 + count2
        data = []
        i = j = 0
        while i < len(leftD) and j < len(rightD):
            if leftD[i] < rightD[j]:
                data.append(leftD[i])
                i += 1
            else:
                data.append(rightD[j])
                count += len(leftD) - i
                j += 1
        if i < len(leftD):
            data.extend(leftD[i:])
        if j < len(rightD):
            data.extend(rightD[j:])
        return data, count%1000000007

if __name__ == "__main__":
    sol = Solution()
    print(sol.InversePairs([1,2,3,4,5,6,7,0]))