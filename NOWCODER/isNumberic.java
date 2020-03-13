import java.util.regex.Pattern;
 
class Solution {
    public boolean isNumeric(String string) {
        String pattern = "^[-+]?\\d*(?:\\.\\d*)?(?:[eE][+\\-]?\\d+)?$";
        String s = new String(string);
        return Pattern.matches(pattern,s);
    }
}

public class isNumberic{
    public static void main(String[] args){
        Solution sol = new Solution();
        System.out.println(sol.isNumeric("12e-19"));
    }
}