import java.util.*;

class Solution {

    Map<Integer, List<Integer>> map = new HashMap<>();
    Random random;

    public void Solution1(int[] nums) {
        random = new Random();
        for (int i = 0; i < nums.length; i++) {
            map.putIfAbsent(nums[i], new ArrayList<>());
            map.get(nums[i]).add(i);
        }
    }

    public int pick1(int target) {
        List<Integer> tmp = map.get(target);
        return tmp.get(random.nextInt(tmp.size()));
    }

    int[] nums;

    public Solution(int[] nums) {
        this.nums = nums;
        random = new Random();
    }

    public int pick(int target) {
        int ans = 0;
        for (int i = 0, cnt = 0; i < nums.length; ++i) {
            if (nums[i] == target) {
                ++cnt;
                if (random.nextInt(cnt) == 0) {
                    ans = i;
                }
            }
        }
        return ans;
    }
}

public class _398 {
    public static void main(String[] args) {
        int[] t1 = new int[]{12, 33, 4, 56, 22, 2, 34, 4, 33, 22, 12, 34, 56};

        Solution solution = new Solution(t1);
        System.out.println(solution.pick(4));
    }
}
