class Solution {
    static String LeftRotateString(String str,int n) {
        int len = str.length();
        if(len == 0)return str;
        String result = str.substring(n%len) + str.substring(0, n%len);
        return result;
    }
}
public class LeftRotateNString {
    public static void main(String[] args) {
        System.out.println(Solution.LeftRotateString("", 6));
    }
}

