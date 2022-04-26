import java.util.Arrays;

public class _883 {
    public int projectionArea(int[][] grid) {
        int xy = 0;
        int zx = 0;
        int[] col = new int[grid.length];
        Arrays.fill(col, 0);
        for (int i = 0; i < grid.length; i++) {
            int lineMax = 0;
            // int cowMax = 0;
            for (int j = 0; j < grid.length; j++) {
                if (grid[i][j] > 0) {
                    xy++;
                }
                lineMax = Math.max(lineMax, grid[i][j]);
                // cowMax = Math.max(cowMax, grid[j][i]);
                col[j] = Math.max(grid[i][j], col[j]);
            }
            zx += lineMax;

        }
        return xy + zx + Arrays.stream(col).sum();
    }

    public static void main(String[] args) {
        int[][] t1 = {{1, 2}, {3, 4}};

        _883 solution = new _883();
        System.out.println(solution.projectionArea(t1));
    }
}
