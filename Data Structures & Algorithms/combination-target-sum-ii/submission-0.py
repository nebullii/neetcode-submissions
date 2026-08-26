class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(current, start, curr_sum):
            if curr_sum == target:
                result.append(current[:])

            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(current + [candidates[i]], i+1, curr_sum + candidates[i])

        backtrack([], 0, 0)
        return result