class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {'[': ']', '{': '}', '(': ')'}

        for i in range(len(s)):
            if s[i] in b_map:
                stack.append(s[i])
            else:
                if not stack or b_map[stack[-1]] != s[i]:
                    return False
                stack.pop()
            
        return len(stack) == 0

