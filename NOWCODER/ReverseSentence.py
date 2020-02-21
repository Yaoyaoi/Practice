class Solution:
    #def ReverseSentence(self, s):
    #    if not s:
    #        return s
    #    s = s[::-1]
    #    start = 0
    #    for i in range(len(s)):
    #        if s[i] == ' ':
    #            s = s[:start] + s[start:i][::-1] +s[i:]
    #            start = i + 1
    #    i += 1
    #    s = s[:start] + s[start:i][::-1] +s[i:]
    #    return s

    def ReverseSentence(self, s):
        sSplited = s.split()
        if not sSplited:
            return s
        return ' '.join(sSplited[::-1])


if __name__ == "__main__":
    s = 'student. a am I'
    sol = Solution()
    print(sol.ReverseSentence(s))