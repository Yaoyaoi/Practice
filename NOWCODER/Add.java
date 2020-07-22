public class Add{
    public int Add(int num1, int num2) {
        int result, ans;
        do {
            result = num1 ^ num2;       // 每一位相加
            ans = (num1 & num2) << 1;   // 进位
            num1 = result;
            num2 = ans;
        } while (ans != 0);
        return result;
    }
    public static void main(String[] args) {
        int a = 10, b = 12;
        Add add = new Add();
        System.out.println(add.Add(10,12));
    }
}