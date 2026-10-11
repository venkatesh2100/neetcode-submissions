class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sub = []

        def dfs(sub , i , tot):

            if tot == target:
                
                res.append(sub[:])
                return 

            elif i >= len(nums) or tot > target:
                return 

            sub.append(nums[i])
            dfs(sub , i , tot + nums[i])
        

            sub.pop()
            dfs(sub , i + 1 , tot)

        dfs(sub , 0 , 0 )

        return res

