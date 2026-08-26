class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return

            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]

                if isPalindrome(substring):
                    backtrack(i, current + [substring])

        backtrack(0, [])
        return result