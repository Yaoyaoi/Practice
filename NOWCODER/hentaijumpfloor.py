class Solution:
    def jumpFloorII(self, number):
        if not number:
            return 0
        return 2**(number-1)



if __name__ == '__main__':
    solution = Solution()
    number = 10
    print(solution.jumpFloorII(number))