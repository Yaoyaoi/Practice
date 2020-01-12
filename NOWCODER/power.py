class Solution:
#    def Power(self, base, exponent):
#        result = 1
#        while exponent:
#            result *= base
#            exponent -= 1
#        return result
    
    def Power(self, base, exponent):
        if not exponent:
            return 1
        result = base
        i = 1
        realExp = exponent
        if exponent < 0:
            exponent = 0 - exponent
        while 2*i <= exponent:
            i *= 2
            result = result * result
        while i < exponent:
            i += 1
            result *= base
        if realExp < 0:
            result = 1/result
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.Power1(2,-3))