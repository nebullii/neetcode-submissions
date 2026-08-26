class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
#Brute Force Way
# Algorithm: Contains Duplicate
# Input: nums
# Output: True if the array comtains duplicate, else False.
# S1: n = size of array
# S2: For i = 0 to n:
# S3:     For j = i+1 to n:
# S4:         If nums[i] = nums[j]:
# S5:             return true
# S6: return False

# Time Complexity for Brute Force: O(n2)
# Time Complexity for Optimal solution: O(n)

#Optimal Solution
# Algorithm: Contains Duplicate
# Input: nums
# Output: True if the array comtains duplicate, else False.
# S1: seen = set()
# S2: For each num in nums:
# S3:     If num in seen:
# S4:         return true
# S6:     Add num in seen
# S7: return false