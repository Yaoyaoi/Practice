import java.util.Arrays;
public class MultiplayArray {
    public int[] multiply(final int[] A) {
        final int[] B = new int[A.length];
        int res = 1;
        for (int i = 0; i < A.length; i++) {
            B[i] = res;
            res *= A[i];
        }
        res = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            B[i] *= res;
            res *= A[i];
        }
        return B;
    }

    public static void main(final String[] args) {
        int[] A = { 1, 2, 3, 4, 5 };
        MultiplayArray ma = new MultiplayArray();
        int[] B = ma.multiply(A);
        System.out.println(Arrays.toString(B));
    }
}