class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l , r = 0 , 0 
        res = 0

        unq = set()
        while r < len(s):
            while s[r] in unq:
                unq.remove(s[l])
                l+=1 


            res = max(res , r - l + 1)
            unq.add(s[r])
            r+=1
        return res