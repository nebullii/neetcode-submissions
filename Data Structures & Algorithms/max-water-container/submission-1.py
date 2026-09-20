class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use 2 pointers l and r
        # at each step, width = r - l and height = min(l, r) => width * height
        n = len(heights)
        l = 0
        r = n - 1
        maxarea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxarea = max(area, maxarea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea