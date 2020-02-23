class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        res = [1]
        t2 = t3 = t5 = 0
        for i in range(index):
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            t2 += 1 if res[-1] == res[t2]*2 else 0
            t3 += 1 if res[-1] == res[t3]*3 else 0
            t5 += 1 if res[-1] == res[t5]*5 else 0
        return res[index-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.GetUglyNumber_Solution(1500))


