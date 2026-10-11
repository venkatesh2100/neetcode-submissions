class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = [ ]

        sub = []

        def backtrack(o , close):

            if o == close == n:
                
                res.append("".join(sub))
                return 

            
            if o < n:
                sub.append("(")
                backtrack(o+1 ,close)
                sub.pop()

            if close < o:
                sub.append(')')
                backtrack(o , close+1)
                sub.pop()

        backtrack(0,0)

            
        return res

