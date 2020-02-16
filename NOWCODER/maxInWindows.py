class Solution:
    #def maxInWindows(self, num, size):
    #    if not num or not size or size > len(num):
    #        return []
    #    def findMax(arr):
    #        maxV = 0
    #        for item in arr:
    #            if item > maxV:
    #                maxV = item
    #        return maxV
    #
    #    windows = num[:size]
    #    maxV = findMax(windows)
    #    result = [maxV]
    #    for item in num[size:]:
    #        windows.append(item)
    #        removedV = windows.pop(0)
    #        if item > maxV:
    #            maxV = item
    #        elif removedV == maxV:
    #            maxV = findMax(windows)
    #        result.append(maxV)
    #    return result

    def maxInWindows(self, num, size):
        queue,res,i = [],[],0
        while size > 0 and i < len(num):
            if queue and queue[0] <= i-size:
                queue.pop(0)
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if i >= size - 1:
                res.append(num[queue[0]])
            i += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxInWindows([2,3,4,2,6,2,5,1],3))

