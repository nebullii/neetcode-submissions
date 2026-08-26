

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        # dfs(start, end, memo=None):
        # first check: start !>= end
        # if memo is none: create memo
        # if memo val is -1, return memo
        # memo[s] is calculated with 3 params reusing memo

        def dfs(s, e, memo=None):
            if s >= e : return 0

            if memo is None:
                memo = [-1] * e

            if memo[s] != -1:
                return memo[s]

            memo[s] = max(dfs(s + 1, e, memo), nums[s] + dfs(s + 2, e, memo))
            return memo[s]


        return max(dfs(0, n - 1), dfs(1, n))