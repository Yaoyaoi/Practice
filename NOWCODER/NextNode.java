
class TreeLinkNode {
    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;

    TreeLinkNode(int val) {
        this.val = val;
    }
}


class Solution {
    static public TreeLinkNode GetNext(TreeLinkNode pNode){
        if(pNode ==null)return pNode;
        if(pNode.right!=null){
            TreeLinkNode node = pNode.right;
            while(node.left!=null){
                node = node.left;
            }
            return node;
        }
        while(true){
            TreeLinkNode parent = pNode.next;
            if (parent==null||parent.left==pNode)return parent;
            pNode = parent;
        }
    }
}

public class NextNode {
    public static void main(String[] args) {
        
    }
}