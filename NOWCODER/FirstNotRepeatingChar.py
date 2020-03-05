class Solution:
    def FirstNotRepeatingChar(self, s):
        hashTable = [0]*58
        for item in s:
            hashTable[ord(item)-65] += 1
        findResult = False
        for i in range(len(s)):
            if hashTable[ord(s[i])-65] == 1:
                findResult = True
                break
        return i if findResult else -1

        #positionQueue = []
        #repeatList = []
        #queue = []
        #for i in range(len(s)):
        #    hasItem = False
        #    if not repeatList.count(s[i]):
        #        for j in range(len(queue)):
        #            if s[i] == queue[j]:
        #                hasItem = True
        #                repeatList.append(queue.pop(j))
        #                positionQueue.pop(j)
        #                break
        #        if not hasItem:
        #            queue.append(s[i])
        #            positionQueue.append(i)
        #return positionQueue[0] if positionQueue else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.FirstNotRepeatingChar('googgle'))