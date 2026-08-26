class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, start):
            result.append(current[:])

            for i in range(start, len(nums)):
                backtrack(current + [nums[i]], i + 1)

        backtrack([], 0)
        return result