class Solution:
    def rob(self, nums: List[int]) -> int:
    # SRTBOT Analysis
    # Subproblem: d[i] = maximum money from house i
    # Recursion: d[i] = max(d[i+1], d[i]+d[i+2])
    # Topology: for i in range(n - 1, -1, -1)
    # Base Case: d[n] = 0 ##no house remain
    # Original Problem: d[0] = the best starting from first

        n = len(nums)
        # Base Case 
        dp = [0] * (n + 2)

        # Topological Order
        for i in range(n - 1, -1, -1):
            # Recursion
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        
        # return original problem
        return dp[0]