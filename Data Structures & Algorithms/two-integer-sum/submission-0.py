class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using hash map
        hash_map = {}
        for i in range(0, len(nums)):
            # Get the complement by subtracting from target
            result = target - nums[i]
            # Check if complement or result is in hash_map
            if result in hash_map:
                return [hash_map[result], i]
            hash_map[nums[i]] = i