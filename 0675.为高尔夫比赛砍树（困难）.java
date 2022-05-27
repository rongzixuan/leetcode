/*
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

0 表示障碍，无法触碰
1 表示地面，可以行走
比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。
 
示例 1：
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。

示例 2：
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。

示例 3：
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。

提示：
m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 10^9

*/


// 方法二：dijkstra算法
// 时间复杂度：O(m * n * log(m * n))
// 空间复杂度：O(m * n)
class Solution {
    int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int bfs(List<List<Integer>> forest, int i, int j, int[] target){
        int target_i = target[0];
        int target_j = target[1];
        //System.out.println(target_i);
        //System.out.println(target_j);

        if (i == target_i && j == target_j){
            return 0;
        }

        int m = forest.size();
        int n = forest.get(0).size();
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>((a, b) -> a[0] - b[0]);
        boolean[][] visited = new boolean[m][n];
        queue.offer(new int[]{0, i * n + j});
        visited[i][j] = true;

        while (!queue.isEmpty()){
            int[] arr = queue.poll();
            int distance = arr[0], loc = arr[1];
            //System.out.println("distance:" + distance);
            //System.out.println("loc:" + loc);
            for (int index = 0; index < 4; ++index){
                int new_i = loc / n + dirs[index][0];
                int new_j = loc % n + dirs[index][1];
                //System.out.println("new_i:" + new_i + "new_j:" + new_j);
                if (0 <= new_i && new_i < m && 0 <= new_j && new_j < n){
                    if (!visited[new_i][new_j] && forest.get(new_i).get(new_j) > 0){
                        if (new_i == target_i && new_j == target_j){
                            return distance + 1;
                        }
                        queue.offer(new int[]{distance + 1, new_i * n + new_j});
                        visited[new_i][new_j] = true;
                    }
                }
            }       
        }
        return -1;
    }

    public int cutOffTree(List<List<Integer>> forest) {        
        List<int[]> trees = new ArrayList<int[]>();
        int m = forest.size();
        int n = forest.get(0).size();

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (forest.get(i).get(j) > 1){
                    trees.add(new int[]{i, j});
                }
            }
        }
        Collections.sort(trees, (a, b) -> forest.get(a[0]).get(a[1]) - forest.get(b[0]).get(b[1]));
        //System.out.println(trees);

        int i = 0;
        int j = 0;
        int ans = 0;
        for (int index = 0; index < trees.size(); ++index){
            //System.out.println("trees.get(index):" + trees.get(index));
            int step = bfs(forest, i, j, trees.get(index));
            //System.out.println("step:" + step);
            if (step == -1){
                return -1;
            }
            ans += step;
            i = trees.get(index)[0];
            j = trees.get(index)[1];
        }
        return ans;
    }
}



