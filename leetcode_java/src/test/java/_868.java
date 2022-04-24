public class _868 {
    public int binaryGap(int n) {
        int gap = 0;
        for (int i = 0, j = -1; i < 31; i++) {
            if ((n & 1) == 1) {
                if (j != -1) {
                    gap = Math.max(gap, i - j);
                }
                j = i;
            }
            n >>= 1;
        }
        return gap;
    }

    public static void main(String[] args) {
        _868 solution = new _868();
        System.out.println(solution.binaryGap(22));
    }
}
