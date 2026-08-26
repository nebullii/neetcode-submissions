class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(current, start):
            result.append(current[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                backtrack(current + [nums[i]], i + 1) 
            
        backtrack([], 0)
        return result