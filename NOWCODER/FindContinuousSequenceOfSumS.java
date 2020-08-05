import java.util.ArrayList;
import java.util.Collections;

class Solution {
    static public ArrayList<ArrayList<Integer>> FindContinuousSequence(final int sum) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        //for (int i = 2; i * (i + 1) / 2 <= sum; i++) {
        //    if (i % 2 == 0) {
        //        if (sum % i * 2 == i) {
        //            int firstNum = sum / i - i / 2 + 1;
        //            ArrayList<Integer> list = new ArrayList<>();
        //            for (int j = 0; j < i; j++) {
        //                list.add(firstNum + j);
        //            }
        //            result.add(list);
        //        }
        //    } else {
        //        if (sum % i == 0) {
        //            int firstNum = sum / i - i / 2;
        //            ArrayList<Integer> list = new ArrayList<>();
        //            for (int j = 0; j < i; j++) {
        //                list.add(firstNum + j);
        //            }
        //            result.add(list);
        //        }
        //    }
        //}
        //Collections.reverse(result);
        //将上面两种情况合成一种 并且添加顺序转变过来
        if(sum<3)return result;
            int s=(int) Math.sqrt(2*sum);
            for(int i = s; i >= 2; i--)
                {
                    if(2 * sum % i == 0)
                        {
                            int d = 2 * sum / i;
                            if(d%2==0&&i%2!=0||d%2!=0&&i%2==0){
                                    int a1=(d-i+1)/2;
                                    int an=(d+i-1)/2;
                                    ArrayList<Integer> list=new ArrayList<Integer>();
                                    for(int j=a1;j<=an;j++)
                                        list.add(j);
                                    result.add(list);
                                }
                        }
                }
        return result;
    }
}

public class FindContinuousSequenceOfSumS {
    public static void main(final String[] args) {
        System.out.println(Solution.FindContinuousSequence(99));
    }
}