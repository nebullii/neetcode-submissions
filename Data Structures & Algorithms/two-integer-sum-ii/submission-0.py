class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        size = len(numbers)
        right = size - 1
        
        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1, right+1]
            elif result < target:
                left += 1
            else: 
                right -= 1

# Algorithm: Two Integer Sum II
# Input: Sorted Array numbers and target
# Output: Return 2 integers that can be equal target
# S0: left = 0
# S1: size = len(numbers)
# S2: right = size - 1

# S3: While left < right:
#     S4: sum = numbers[left] + numbers[right]
#     S5: If sum == target:
#         S6: return [left + 1, right + 1]  # Convert to 1-based index
#     S7: Else if sum < target:
#         S8: left += 1  # Move left pointer right to get a larger sum
#     S9: Else:
#         S10: right -= 1  # Move right pointer left to get a smaller sum
