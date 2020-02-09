class Solution:
    # 方法一
    #def MoreThanHalfNum_Solution(self, numbers):
    #    if not numbers:
    #        return 0
    #    numbers.sort()
    #    j = len(numbers)//2
    #    i = j + 1
    #    target = numbers[j]
    #    count = 0
    #    while i < len(numbers) and numbers[i] == target:
    #        count += 1
    #        i += 1
    #    while j > -1 and numbers[j] == target:
    #        count += 1
    #        j -= 1
    #    return target if count > len(numbers)/2 else 0
    
    # 方法二： 打擂算法
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        host = numbers[0]
        count = 1
        for item in numbers[1:]:
            if item == host:
                count += 1
            else:
                count -= 1
                if not count:
                    count = 1
                    host = item
        count = 0
        for item in numbers:
            if item == host:
                count+=1
        return host if count*2>len(numbers) else 0

if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    sol = Solution()
    print(sol.MoreThanHalfNum_Solution(numbers))