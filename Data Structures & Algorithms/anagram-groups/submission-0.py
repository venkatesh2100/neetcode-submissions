class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hmap = {}

        for i in range(len(strs)):

            sval = tuple(sorted(strs[i]))
            # print(sval)

            if sval in hmap:
                hmap[sval].append(strs[i])
            else:
                hmap[sval] = [strs[i]]

        # print(hmap)
        return list(hmap.values())
            