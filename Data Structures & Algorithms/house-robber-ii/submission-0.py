class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        if n == 1: return nums[0]


        def solve(nums):
            m = len(nums)
            memo = [-1] * m
            def dfs(i):
                if i >= m: return 0
                if memo[i] != -1: return memo[i]
                memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
                return memo[i]
            return dfs(0)
        return max(solve(nums[1:]), solve(nums[:-1]))
