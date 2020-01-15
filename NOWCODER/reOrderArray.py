class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        oddArray = []
        evenArray = []
        for item in array:
            if item%2 == 0:
                evenArray.append(item)
            else:
                oddArray.append(item)
        oddArray.extend(evenArray)
        return oddArray

if __name__ == '__main__':
    array = [1,4,5,3,6,7,8,9]
    sol = Solution()
    print(sol.reOrderArray(array))