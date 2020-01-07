class Solution:
    def jumpFloor(self, number):
        if number == 0 :
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        F = [1, 1]
        for i in range(2,number+1):
            F[i%2] = F[i%2] + F[(i+1)%2]
        return F[i%2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloor(5))