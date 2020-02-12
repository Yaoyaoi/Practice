import java.util.ArrayList;

public class GetLeastKNumbers {
    public ArrayList<Integer> GetLeastNumbers_Solution(int[] input, int k) {
        ArrayList<Integer> list = new ArrayList<Integer>();

        if (input == null || k > input.length || k <= 0)
            return list;
        int[] target = new int[k];
        int len = input.length;
        for (int i = 0; i < len; ++i) {
            if (i < k) {
                target[i] = input[i];
                heapInsertSiftUp(target, i, target[i]);
            } else {
                if (target[0] > input[i]) { // 最大堆下沉
                    target[0] = input[i];
                    siftDown(target, 0, target[0]);
                    // 相比优先级队列，这里不会offer操作(里面有上浮)，少了一步上浮调整，效率高了不止一丁点
                }
            }
        }
        for (int i = 0; i < k; ++i) {
            list.add(target[i]);
        }
        return list;
    }

    private void heapInsertSiftUp(int[] target, int index, int x) {
        while (index > 0) {
            int parent = (index - 1) >>> 1;
            if (greater(x, target[parent])) {
                target[index] = target[parent]; // 往下拉，避免直接上浮覆盖前面的值
                index = parent;
            } else {
                break;
            }
        }
        target[index] = x;
    }

    private boolean greater(int i, int j) {
        return i > j;
    }

    private void siftDown(int[] target, int k, int x) {
        int half = target.length >>> 1;
        while (k < half) {
            int child = (k << 1) + 1; // 默认先左孩子
            int big = target[child];
            int right = child + 1;
            if (right < target.length && greater(target[right], big)) {
                big = target[right];
                child = right; // 可以直接一步big = target[child = right];
            }
            if (greater(x, big)) // x比子节点中的最大值还大，已经是大顶堆了
                break; // 往上拉不动了，准备退出把最初堆顶的结点赋值到上一个结点
            target[k] = big; // 往上拉
            k = child;
        }
        target[k] = x;
    }
    public static void main(String[] args){
        int[] input = {4,5,1,6,2,7,3,8};
        GetLeastKNumbers gln = new GetLeastKNumbers();
        System.out.println(gln.GetLeastNumbers_Solution(input,4));
    }
}


