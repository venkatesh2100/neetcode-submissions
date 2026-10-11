class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

       
        hmap = {}

        for i in range(len(nums)):

            val = target - nums[i]

            if val in hmap:
                return [ hmap[val], i]

            else:
                hmap[nums[i]] = i

        
        return [-1,-1]

