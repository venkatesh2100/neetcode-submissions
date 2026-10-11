class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        #Approach -1  Using Two hashmaps 
        # hmap1 , hmap2 = {} , {} 
        if len(s) != len(t): return False

        # for i in range(len(s)):

        #     hmap1[s[i]] = hmap1.get(s[i] , 0) + 1

        #     hmap2[t[i]] = hmap2.get(t[i] , 0) + 1 

        # return hmap1 == hmap2


        # s1 = sorted(s) 
        # s2 = sorted(t)

        # return s1 == s2




        hmap = defaultdict(int)

        for i in range(len(s)):

            hmap[s[i]] = hmap.get(s[i] , 0) + 1
            hmap[t[i]] = hmap.get(t[i] , 0) - 1

        for v in hmap.values():
            if v != 0: return False 

        return True