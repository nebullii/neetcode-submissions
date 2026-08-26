class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen_map:
                last_seen = seen_map[s[right]]
                if last_seen >= left:
                    left = last_seen + 1
            seen_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len





        # left = 0
        # max_len = 0
        # seen = set()

        # for right in range(len(s)):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1
        #     seen.add(s[right])
        #     max_len = max(max_len, right - left + 1)
        
        # return max_len

