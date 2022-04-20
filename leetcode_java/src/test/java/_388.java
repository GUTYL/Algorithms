import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class _388 {
    public int lengthLongestPath(String input) {
        Map<Integer, Integer> depthLengthMap = new HashMap<>();
        depthLengthMap.put(-1, 0);
        int maxLen = 0;
        for (String line : input.split("\n")) {
            int depth = line.length() - line.replaceAll("\t", "").length();
            depthLengthMap.put(depth, depthLengthMap.get(depth - 1) + line.length() - depth);
            if (line.contains(".")) {
                maxLen = Math.max(maxLen, depthLengthMap.get(depth) + depth);
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        _388 s = new _388();
        System.out.println(s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"));


    }
}
