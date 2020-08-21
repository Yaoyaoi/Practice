import java.util.ArrayList;
class Solution {
    public static ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList<Integer> ans = new ArrayList<>();
        if (sum==0||array == null||array.length==1)return null;
        int i = 0;
        int j = array.length-1;
        while(i<j){
            if (array[i]+array[j]<sum)i++;
            if (array[i]+array[j]>sum)j--;
            if (array[i]+array[j]==sum){
                ans.add(array[i]);
                ans.add(array[j]);
                return ans;
            }
        }
        return ans;
    }
}
public class FindNumbersWithSumS{
    public static void main(String[] args) {
        System.out.println(Solution.FindNumbersWithSum(new int[]{1,2,4,7,11,15},15));
    }
}