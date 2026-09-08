from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
    # SRTBOT Analysis
    # Subproblem: d[i] = maximum money from house i
    # Recursion: d[i] = max(d[i+1], d[i]+d[i+2])
    # Topology: for i in range(n - 1, -1, -1)
    # Base Case: d[n] = 0 ##no house remain
    # Original Problem: d[0] = the best starting from first

        n = len(nums)

        # dp = [0] * (n + 2)

        # for i in range(n - 1, -1, -1):
        #     dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        
        # return dp[0]
        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= n: return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        return dfs(0)