/*
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

示例 1：
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

示例 2：
输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]

示例 3：
输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
 
提示：
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

*/


// 方法二：原地修改 + 位运算
// 时间复杂度：O(n)
// 空间复杂度：O(1)
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {

        for(int i = 0; i < 2 * n; i ++){
            int j = i < n ? 2 * i : 2 * (i - n) + 1;
            nums[j] |= (nums[i] & 1023) << 10;
        }
        for(int& e: nums) e >>= 10;
        return nums;
    }
};


// 方法三：原地修改
// 时间复杂度：O(n)
// 空间复杂度：O(1)
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {

        for(int i = 0; i < 2 * n; i ++)
            if(nums[i] > 0){
                
                // j 描述当前的 nums[i] 对应的索引，初始为 i
                int j = i; 

                while(nums[i] > 0){

                    // 计算 j 索引的元素，也就是现在的 nums[i]，应该放置的索引
                    j = j < n ? 2 * j : 2 * (j - n) + 1; 

                    // 把 nums[i] 放置到 j 的位置，
                    // 同时，把 nums[j] 放到 i 的位置，在下一轮循环继续处理
                    swap(nums[i], nums[j]); 

                    // 使用负号标记上，现在 j 位置存储的元素已经是正确的元素了 
                    nums[j] = -nums[j]; 
                }
            }

        for(int& e: nums) e = -e;
        return nums;
    }
};



