class Solution:
    # 方法一排完不是字典序
    #def __init__(self):
    #    self.result = []
    #def Permutation(self, ss):
    #    if not ss:
    #        return []
    #    if len(ss) == 1:
    #        return [ss]
    #    self.PermutationRe(0, ss)
    #    return self.result
    #
    #def PermutationRe(self, index, ss):
    #    if index == len(ss)-1:
    #        self.result.append(ss)
    #        return
    #    self.PermutationRe(index+1, ss)
    #    for i in range(index+1,len(ss)):
    #        if ss[index] != ss[i]:
    #            temp = ss[index]
    #            sss = ss[:index] + ss[i] + ss[index+1:i] + ss[index] + ss[i+1:]
    #            self.PermutationRe(index+1, sss)
        
    def Permutation(self, ss):
        if not ss:
            return []
        result = []
        ssList = list(ss)
        ssList.sort()
        result.append(''.join(ssList))
        while True:
            # find where ssList[i] < ssList[i+1]
            i = len(ssList)-2
            while(i > -1):
                if ssList[i] < ssList[i+1]:
                    break
                i -= 1
            if i == -1:
                break
            
            # find minIndex
            minIndex = i+1
            for j in range(i+1,len(ssList)):
                if ssList[j] > ssList[i] and ssList[j] < ssList[minIndex]:
                    minIndex = j

            # swap i and minIndex
            temp = ssList[minIndex]
            ssList[minIndex] = ssList[i]
            ssList[i] = temp

            #sort
            tempList = ssList[i+1:]
            tempList.sort()
            ssList = ssList[:i+1] + tempList
            result.append(''.join(ssList))
        return result

if __name__ == "__main__":
    ss =  'aaab'
    sol = Solution()
    print(sol.Permutation(ss))