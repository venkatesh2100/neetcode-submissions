class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        hmap = {}

        for i in range(len(nums)):

            hmap[nums[i]] = hmap.get(nums[i], 0 ) + 1


        val = sorted(hmap.items() , key = lambda x:x[1], reverse = True )

        # print(val)
        arr = []
        i = 0
        while k:
            arr.append(val[i][0])
            k-=1
            i+=1
        
        return arr
