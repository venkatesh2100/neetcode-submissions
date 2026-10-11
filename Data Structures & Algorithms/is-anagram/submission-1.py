class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        #Approach -1  Using Two hashmaps 
        # hmap1 , hmap2 = {} , {} 
        # if len(s) != len(t): return False

        # for i in range(len(s)):

        #     hmap1[s[i]] = hmap1.get(s[i] , 0) + 1

        #     hmap2[t[i]] = hmap2.get(t[i] , 0) + 1 

        # return hmap1 == hmap2


        s1 = sorted(s) 
        s2 = sorted(t)

        return s1 == s2