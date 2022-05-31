"""
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:


        # 方法一：深度优先搜索
        # 时间复杂度:O(m * n)
        # 空间复杂度：O(m * n)，栈的开销
        m, n = len(image), len(image[0])
        initColor = image[sr][sc]

        def dfs(i, j):
            image[i][j] = newColor

            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    if image[new_i][new_j] == initColor:
                        dfs(new_i, new_j)

        if image[sr][sc] != newColor:
            dfs(sr, sc)
        return image


        # 方法二：广度优先搜索
        # 时间复杂度:O(m * n)
        # 空间复杂度：O(m * n)，队列的开销
        m, n = len(image), len(image[0])
        initColor = image[sr][sc]

        if image[sr][sc] == newColor:
            return image

        queue = [(sr, sc)]

        while queue:
            i, j = queue.pop(0)
            image[i][j] = newColor

            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n and image[new_i][new_j] == initColor:
                    queue.append((new_i, new_j))

        return image


