class Solution:
    def PrintMinNumber(self, numbers):
        def compare(str1,str2):
            str3 = str1 + str2
            str4 = str2 + str1
            return str3 > str4 
        numbers = list(map(str,numbers))
        for i in range(len(numbers)-1,-1,-1):
            for j in range(i):
                if compare(numbers[j],numbers[j+1]):
                    temp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j+1] = temp
        return ''.join(numbers)
    #def PrintMinNumber(self, numbers):
    #    return self.MinNumber(numbers,0)
    #
    #def MinNumber(self, numbers, i):
    #    strNum = ''
    #    numbers = list(map(str, numbers))
    #    while  len(numbers) > 1:
    #        minI = 0
    #        maxL = 0
    #        for j in range(len(numbers)):
    #            if i == len(numbers[j]):
    #                numbers[j] = '0' + numbers[j]
    #            if i < len(numbers[j]) and numbers[j][i] < numbers[minI][i]:
    #                minI = j
    #        minList = []
    #        j = minI
    #        minValue = numbers[minI][i]
    #        while (j < len(numbers)):
    #            if numbers[j][i] == minValue:
    #                if len(numbers[j]) > maxL:
    #                    maxL = len(numbers[j])
    #                minList.append(numbers[j])
    #                numbers.pop(j)
    #            else:
    #                j += 1
    #        if i + 1 < maxL:
    #            strNum += self.MinNumber(minList, i+1)
    #        else:
    #            strNum += ''.join(list(map(str,list(map(int,minList)))))
    #    if numbers:
    #        strNum += str(int(numbers[0]))
    #    return strNum

if __name__ == "__main__":
    sol = Solution()
    print(sol.PrintMinNumber([3,32,321]))