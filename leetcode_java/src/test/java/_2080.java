import java.util.*;
import java.util.stream.Collectors;

class RangeFreqQuery {
    static List<Integer> arrs = null;

    public void RangeFreqQuery1(int[] arr) {
        arrs = Arrays.stream(arr).boxed().collect(Collectors.toList());
    }

    public int query1(int left, int right, int value) {
        List<Integer> tmp = arrs.subList(left, right + 1);
        return Collections.frequency(tmp, value);
    }

    Map<Integer, List<Integer>> map = new HashMap<>();

    public RangeFreqQuery(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            List<Integer> list = map.getOrDefault(arr[i], new ArrayList<>());
            list.add(i);
            map.put(arr[i], list);
        }
    }

    public int query(int left, int right, int value) {
        if (!map.containsKey(value)) {
            return 0;
        }
        int l = bis_left(map.get(value), left);
        int r = bis_right(map.get(value), right);
        return r - l;
    }

    private int bis_right(List<Integer> values, int target) {
        int n = values.size();
        int left = 0;
        int right = n;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (values.get(mid) > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
            // if (target >= values.get(mid)) {
            //     left = mid + 1;
            // } else {
            //     right = mid;
            // }
        }
        return left;
    }

    private int bis_left(List<Integer> values, int target) {
        int n = values.size();
        int left = 0;
        int right = n;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (values.get(mid) >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
            // if (target <= values.get(mid)) {
            //    right = mid;
            // } else {
            //     left = mid + 1;
            // }
        }
        return left;
    }
}

public class _2080 {
    public static void main(String[] args) {
        int[] t1 = new int[]{12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56};

        RangeFreqQuery solution = new RangeFreqQuery(t1);
        System.out.println(solution.query(1, 2, 4));
    }
}
