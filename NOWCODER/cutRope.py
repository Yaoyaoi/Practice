class Solution:
    # 动态规划
    #def cutRope(self, number):
    #    resultList = [0, 1]
    #    for i in range(1,number+1):
    #        if i == 1:
    #            continue
    #        maxRe = 0
    #        for j in range(1,i//2+1):
    #            n1 = resultList[j] if resultList[j] > j else j
    #            n2 = resultList[i - j] if resultList[i - j] > i - j else i - j
    #            maxRe = n1*n2 if n1*n2 > maxRe else maxRe
    #        resultList.append(maxRe)
    #    return resultList[number]
    # 贪心算法
    def cutRope(self, number):
        if number < 2: return 0
        if number == 2:return 1
        if number == 3:return 2
        timesof3 = number // 3
        if number - timesof3 * 3 == 1:
            timesof3 -= 1
        timesof2 = (number - timesof3 * 3) // 2
        return (3**timesof3)*(2**timesof2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.cutRope(8))