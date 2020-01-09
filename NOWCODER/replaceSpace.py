class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        result = ''
        for i in s:
            if i == ' ':
                result += '%20'
            else:
                result += i
        return result


if __name__ == '__main__':
    s = '   '
    sol = Solution()
    print(sol.replaceSpace(s))