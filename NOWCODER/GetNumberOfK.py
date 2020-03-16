class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        if k < data[0] or k > data[-1]:
            return 0
        l = 0
        h = len(data)
        while l != h:
            mid = (l+h)//2
            if data[mid] == k:
                l = h = mid
            elif data[mid] < k:
                l = mid + 1
            else:
                h = mid - 1
        count = 0
        if data[l] == k:
            count += 1
            i = l - 1
            j = l + 1
            while i >= 0 and data[i] == k:
                count += 1
                i -= 1
            while j < len(data) and data[j] == k:
                count += 1
                j += 1
        return count
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.GetNumberOfK([4,4,5,6],4))