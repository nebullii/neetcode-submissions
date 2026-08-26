class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countS = {}
        countT = Counter(t)
        resLen = float('inf')
        res = [-1, -1]
        have = 0
        need = len(countT)
        l = 0

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
                
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""

        
