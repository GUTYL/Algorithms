import java.util.ArrayList;
import java.util.List;


// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


public class _1305 {
    List<Integer> result = new ArrayList<>();

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> nums0 = new ArrayList<>();
        List<Integer> nums1 = new ArrayList<>();

        inOrder(root1, nums0);
        inOrder(root2, nums1);

        int p0 = 0;
        int p1 = 0;

        while (p0 < nums0.size() && p1 < nums1.size()) {
            if (nums0.get(p0) < nums1.get(p1)) {
                result.add(nums0.get(p0));
                p0++;
            } else {
                result.add(nums1.get(p1));
                p1++;
            }
        }
        if (p0 < nums0.size()) {
            result.addAll(nums0.subList(p0, nums0.size()));
        }
        if (p1 < nums1.size()) {
            result.addAll(nums1.subList(p1, nums1.size()));
        }

        return result;
    }

    private void inOrder(TreeNode root, List<Integer> nums) {
        if (root == null) {
            return;
        }
        inOrder(root.left, nums);
        nums.add(root.val);
        inOrder(root.right, nums);
    }

    public static void main(String[] args) {
        TreeNode root1 = null;
        TreeNode root2 = null;
        _1305 solution = new _1305();
        System.out.println(solution.getAllElements(root1, root2));
    }
}
