import java.util.ArrayList;
import java.util.List;

public class _386 {
    List<Integer> result = new ArrayList<>();

    public List<Integer> lexicalOrder(int n) {
        for (int i = 1; i <= 9; i++) {
            dfs(i, n);
        }
        return result;
    }

    private void dfs(int cur, int limit) {
        if (cur > limit) {
            return;
        }
        result.add(cur);
        for (int i = 1; i <= 9; i++) {
            dfs(cur * 10 + i, limit);
        }
    }

    public static void main(String[] args) {
        _386 s = new _386();
        s.lexicalOrder(11);
    }
}
