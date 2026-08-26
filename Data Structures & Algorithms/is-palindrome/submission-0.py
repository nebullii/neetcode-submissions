class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase versions
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True




        # s = ''.join(c.lower() for c in s if c.isalnum())
        # return s == s[::-1]

# Algorithm: Valid Palindrome
# Input: s
# Output: True if the given string is a valid palindrom, false otherwise.
# S1: Remove spaces and special characters
# S2: if s[1:] == s[-1:]
#     S3: return True
# S4: else: 
#     S5: return False