import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

import javax.lang.model.element.Element;

import apple.laf.JRSUIUtils.Tree;

class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;
    }
}
class Solution {
    static ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        if(pRoot==null)return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(pRoot);
        while(!queue.isEmpty()){
            int sz = queue.size();
            ArrayList<Integer> layerList = new ArrayList<>();
            while(sz-->0){
                TreeNode temp = queue.poll();
                layerList.add(temp.val);
                if(temp.left!=null)queue.offer(temp.left);
                if(temp.right!=null)queue.offer(temp.right);
            }
            result.add(layerList);
        }
        return result;
    }
}

public class PrintTreeByLine{
    public static void main(String[] args) {
        TreeNode pRoot = new TreeNode(0);
        pRoot.left = new TreeNode(1);
        pRoot.right = new TreeNode(2);
        //ArrayList res = Solution.Print(pRoot);
        System.out.println(Solution.Print(pRoot));
    }
}