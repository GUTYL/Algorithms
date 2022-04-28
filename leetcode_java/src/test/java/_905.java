import java.util.Arrays;

public class _905 {
    public int[] sortArrayByParity1(int[] nums) {
        int front = 0;
        int after = nums.length - 1;
        while (front < after) {
            // 前 找奇数
            while (front < after && nums[front] % 2 == 0) {
                front++;
            }
            if (after == front) {
                continue;
            }
            // 后 找偶数
            while (front < after && nums[after] % 2 != 0) {
                after--;
            }
            if (front < after) {
                int tmp = nums[front];
                nums[front] = nums[after];
                nums[after] = tmp;
            }
        }
        return nums;
    }

    public int[] sortArrayByParity(int[] nums) {
        int j = nums.length - 1;
        for (int i = 0; i < j; i++) {
            if (nums[i] % 2 == 1) {
                int tmp = nums[j];
                nums[j--] = nums[i];
                nums[i--] = tmp;
            }
        }
        return nums;
    }


    public static void main(String[] args) {
        int[] t1 = new int[]{1, 2, 3, 4};

        _905 solution = new _905();
        System.out.println(Arrays.toString(solution.sortArrayByParity(t1)));
    }
}
