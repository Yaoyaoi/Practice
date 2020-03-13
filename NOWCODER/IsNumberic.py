class Solution:
    # s字符串
    def isNumeric(self, s):
        sSplited = s.split('e')
        if len(sSplited) > 2:
            return False
        if len(sSplited) == 1:
            sSplited = sSplited[0].split('E')
        if len(sSplited) > 2:
            return False
        for j in range(len(sSplited)):
            item = sSplited[j]
            countDot = j
            if item:
                if not item[0].isdigit():
                    if item[0] != '+' and item[0] != '-':
                        return False
            else:
                return False
            for i in range(1,len(item)):
                if item[i].isalpha():
                    return False
                if not item[i].isdigit():
                    if item[i] == '.':
                        countDot += 1
                    if item[i] != '.' or countDot > 1:
                        return False
        return True
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.isNumeric("100"))
