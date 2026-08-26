class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        size = len(nums)
        result = []

        # Step 2: Edge case for exactly 3 elements
        if size == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        # Step 3: Iterate through the array
        for i in range(size - 2):
            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = size - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

        
