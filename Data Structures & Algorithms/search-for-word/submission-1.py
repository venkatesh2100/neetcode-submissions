class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dic = [(0,1) , (1,0) , (-1,0) , (0,-1)]

        vis = set()
        def backtrack(r ,c , i):

            if  i == len(word):
                return True 

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False 

            if board[r][c] != word[i]:
                return False

            if ( r , c) in vis:
                return False 

            vis.add((r,c))
            for dr , dc in dic:

                if backtrack(r + dr , c + dc , i+1):
                    return True 
            vis.remove((r,c))


        for r in range(len(board)):
            for c in range(len(board[0])):


                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True 

        return False



        
        
