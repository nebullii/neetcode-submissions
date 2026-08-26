class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = Counter(t)
        window_count = defaultdict(int)
        left, right = 0, 0
        formed = 0
        min_len = float('inf')
        start_index = 0

        while right < len(s):
            window_count[s[right]] += 1
            if s[right] in target and window_count[s[right]] == target[s[right]]:
                formed += 1
            while formed == len(target):
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start_index = left
                window_count[s[left]] -= 1

                if s[left] in target and window_count[s[left]] < target[s[left]]:
                    formed -= 1
                left += 1
            right += 1

        if min_len == float('inf'):
            return ""
        return s[start_index:start_index + min_len]
         



        