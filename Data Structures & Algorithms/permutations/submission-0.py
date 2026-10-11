class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        used = [False] * len(nums)

        def dfs():
            if len(sub) == len(nums):
                res.append(sub[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                sub.append(nums[i])

                dfs()

                sub.pop()
                used[i] = False

        dfs()
        return res