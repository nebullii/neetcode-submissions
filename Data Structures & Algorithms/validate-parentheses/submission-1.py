class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'[': ']', '{': '}', '[': ']', '(': ')'}

        for b in s:
            if b in pair:
                stack.append(b)
            else:
                if not stack or pair[stack[-1]] != b:
                    return False
                stack.pop()

        return len(stack) == 0
        