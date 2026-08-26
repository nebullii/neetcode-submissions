class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(current, start, curr_sum):
            if curr_sum == target:
                result.append(current[:])
                return

            if curr_sum > target:
                return

            for i in range(start, len(nums)):
                backtrack(current + [nums[i]], i, curr_sum + nums[i])

        backtrack([], 0, 0)
        return result
