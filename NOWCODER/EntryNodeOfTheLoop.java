
class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ListNode EntryNodeOfLoop(ListNode pHead){
        if(pHead==null||pHead.next==null)return null;
        ListNode p1 = pHead;
        ListNode p2 = pHead;
        while(p2!=null && p1!=null){
            p1 = p1.next;//慢指针 一次一步
            p2 = p2.next.next;//快指针 一次两步
            if(p1 == p2){
                p1 = pHead;
                while(p1!=p2){
                    p1 = p1.next;
                    p2 = p2.next;
                }
                if(p1 == p2){
                    return p1;
                }
            }
        }
        return null;
    }
}


public class EntryNodeOfTheLoop {
   public static void main(String[] args) {
       
   }
}