import java.util.LinkedList;
import java.util.HashMap;


class Solution {
    //Insert one char from stringstream
    //ArrayList <Charater> charList = new ArrayList<>();
    //LinkedList <Character>listOfCharAppearOnce = new LinkedList<>();
    LinkedList <Character>listOfChar = new LinkedList<>();
    HashMap<Character,Integer>countHM = new HashMap<>();
    public void Insert(char ch){
        int count = 0;
        if (countHM.containsKey(ch)){
            count = (Integer)countHM.get(ch);
        }
        countHM.put(ch, count+1);
        listOfChar.offer(ch);
        /*if (countHM.containsKey(ch)){
            count = (Integer)countHM.get(ch);
            if(count==1){
                for (Character C:listOfCharAppearOnce){
                    if (C.charValue()==ch){
                        listOfCharAppearOnce.remove(C);
                        break;
                    }
                }
            }
        }else{
            listOfCharAppearOnce.add(ch);
        }
        countHM.put(ch, count+1);
        */
    }
  //return the first appearence once char in current stringstream
    public char FirstAppearingOnce(){
        while(!listOfChar.isEmpty()){
            char ch = listOfChar.peek();
            int count = (Integer)countHM.get(ch);
            if(count!=1){
                listOfChar.poll();
            }else{
                return ch;
            }
        }
        return '#';
        /*if (listOfCharAppearOnce.isEmpty()){
            return '#';
        }else{
            return listOfCharAppearOnce.getFirst().charValue();
        }*/
        
    }
}
public class FirstCharAppearingOnce {
    public static void main(String[] args) {
        Solution solu = new Solution();
        solu.Insert('g');
        System.out.println(solu.FirstAppearingOnce());
        solu.Insert('o');
        System.out.println(solu.FirstAppearingOnce());
        solu.Insert('o');
        System.out.println(solu.FirstAppearingOnce());;
        solu.Insert('g');
        System.out.println(solu.FirstAppearingOnce());;
        solu.Insert('l');
        System.out.println(solu.FirstAppearingOnce());
        solu.Insert('e');
        System.out.println(solu.FirstAppearingOnce());

    }
}