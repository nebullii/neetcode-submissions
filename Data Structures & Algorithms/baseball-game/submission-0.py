class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == '+':
                stack.append(stack[-1] + stack[-2])
            elif ops == 'D' and stack:
                stack.append(2 * stack[-1])
            elif ops == 'C' and operations:
                stack.pop()
            else:
                stack.append(int(ops))
        return sum(stack)
            