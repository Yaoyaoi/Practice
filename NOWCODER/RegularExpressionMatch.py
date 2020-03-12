class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == '' and pattern == '':
            return True
        if pattern == '':
            return False
        if 1 < len(pattern) and pattern[1] == '*':
            if s == '':
                return self.match(s, pattern[2:])
            match = False
            if pattern[0] == '.' or s[0] == pattern[0]:
                match = self.match(s[1:],pattern)
                if not match:
                    match = self.match(s[1:],pattern[2:])
            if not match:
                match = self.match(s,pattern[2:])
            return match
        elif s == '':
            return False
        elif s[0] == pattern[0] or pattern[0]=='.':
            return self.match(s[1:],pattern[1:])
        else:
            return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.match("bbbba",".*a*a"))

