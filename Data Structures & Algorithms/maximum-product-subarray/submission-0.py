class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # Subproblem
        max_dp = [0] * n
        min_dp = [0] * n
        result = nums[0]
        # Base Case
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        # Topological Order
        for i in range(1, n):
            # Recurrence Relation
            max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])
            min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])
            result = max(result, max_dp[i])
        # Original Problem
        return result
