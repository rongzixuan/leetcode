/*
我们有两个长度相等且不为空的整型数组 nums1 和 nums2 。在一次操作中，我们可以交换 nums1[i] 和 nums2[i]的元素。
例如，如果 nums1 = [1,2,3,8] ， nums2 =[5,6,7,4] ，你可以交换 i = 3 处的元素，得到 nums1 =[1,2,3,4] 和 nums2 =[5,6,7,8] 。
返回 使 nums1 和 nums2 严格递增 所需操作的最小次数 。

数组 arr 严格递增 且  arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1] 。

注意：
用例保证可以实现操作。

示例 1:
输入: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
输出: 1
解释: 
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。

示例 2:
输入: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
输出: 1

提示:
2 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 2 * 10^5

*/

class Solution {
    public int minSwap(int[] nums1, int[] nums2) {


        // 方法一：状态机动态规划
        // 时间复杂度：O(n)
        // 空间复杂度：O(n)
        int[][] dp = new int[nums1.length][2];
        dp[0][0] = 0; dp[0][1] = 1;
        for (int i = 1; i < nums1.length; i++) {
            int a1 = nums1[i - 1], a2 = nums1[i], b1 = nums2[i - 1], b2 = nums2[i];
            if ((a1 < a2 && b1 < b2) && (b1 < a2 && a1 < b2)) {
                dp[i][0] = Math.min(dp[i - 1][0], dp[i - 1][1]); // 如果i【不互换】，则i-1可【互换】也可【不互换】
                dp[i][1] = dp[i][0] + 1; // 如果i【互换】，则i-1可【互换】也可【不互换】
            } else if (a1 < a2 && b1 < b2) {
                dp[i][0] = dp[i - 1][0]; // 如果i【不互换】，则i-1必须【不互换】
                dp[i][1] = dp[i - 1][1] + 1; // 如果i【互换】，则i-1必须【互换】
            } else {
                dp[i][0] = dp[i - 1][1]; // 如果i【不互换】，则i-1必须【互换】
                dp[i][1] = dp[i - 1][0] + 1; // 如果i【互换】，则i-1必须【不互换】
            }
        }
        return Math.min(dp[nums1.length - 1][0], dp[nums1.length - 1][1]);
    }
}

