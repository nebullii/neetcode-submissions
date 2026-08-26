class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1