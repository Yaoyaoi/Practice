
class Solution:
    def NumberOf1(self, n): # 一个一个数
        # write code here
        if n<0:
            n=n&0xffffffff  # 变成补码 
        return bin(n).count("1")

    def NumberOf12(self, n):
        # write code here
        count=0
        if n < 0:
            n = n & 0xffffffff
        while n!=0:
            n=n&(n-1)
            count+=1
        return count

# Java
# 方法1
#public class Solution {
#    public int NumberOf1(int n) {
#        int count = 0;
#        int flag = 1;
#        while (flag != 0) {
#            if ((n & flag) != 0) {
#                count++;
#            }
#            flag =flag << 1;
#        }
#        return count;
#    }
#}
# 方法2
#public class Solution {
#    public int NumberOf1(int n) {
#        int count = 0;
#        while(n!= 0){
#            count++;
#            n = n & (n - 1);
#         }
#        return count;
#    }
#}

if __name__ == '__main__':
    number = -1
    sol = Solution()
    print(sol.NumberOf1(number))