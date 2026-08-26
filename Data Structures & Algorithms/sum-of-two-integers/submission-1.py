class Solution:
    def getSum(self, a: int, b: int) -> int:
        M = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & M
            b = carry & M
        return a if a <= 0x7FFFFFFF else ~(a ^ M)