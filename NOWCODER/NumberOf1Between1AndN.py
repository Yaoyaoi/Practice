# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        num = n
        count = 0
        count1 = 1
        i = 0
        while n:
            a = n % 10
            if not i:
                n = n//10
                i += 1
                if a:
                    count += 1
                continue
            if a:
                if a == 1:
                    count += num%(10**i)+1 
                    count += count1
                else:
                    count += count1 * a + 10**i
            count1 = 10 * count1 + 10**i
            n = n // 10
            i += 1
        return count

    

if __name__ == "__main__":
    num = int(input())
    sol = Solution()
    print(sol.NumberOf1Between1AndN_Solution(num))
