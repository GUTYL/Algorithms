import java.util.Arrays;

public class _821 {

    public int[] shortestToChar(String s, char c) {
        int length = s.length();
        int[] result = new int[length];
        Arrays.fill(result, length + 1);
        for (int i = 0, j = -1; i < length; i++) {
            if (s.charAt(i) == c) {
                j = i;
            }
            if (j != -1) {
                result[i] = i - j;
            }
        }

        for (int i = length - 1, j = -1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                j = i;
            }
            if (j != -1) {
                result[i] = Math.min(result[i], j - i);
            }
        }
        return result;

    }

    public static void main(String[] args) {
        _821 s = new _821();
        System.out.println(Arrays.toString(s.shortestToChar("loveleetcode", 'e')));
    }
}

