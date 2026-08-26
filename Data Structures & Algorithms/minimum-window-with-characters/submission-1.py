class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = Counter(t) # count letter frequency in t
        countS = {} # initialize empty hash to store substring letter frequency
        have = 0 # how many letters we have in current window
        need = len(countT) # what is the min length we need
        res = [-1, -1] # a variable to store result
        resLen = float('inf') 
        l = 0 # left pointer

        for r in range(len(s)): # loop through entire s
            countS[s[r]] = 1 + countS.get(s[r], 0) # add frequency count of s[r]
            if s[r] in countT and countS[s[r]] == countT[s[r]]: #if char and frequency match with t
                have += 1 # increment have
            
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

            
