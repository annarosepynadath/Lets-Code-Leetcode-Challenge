class Solution:
    def maxDepth(self, s: str) -> int:
        max=0
        count=0
        for x in s:
            if (x=='('):
                count+=1
                if(count>max):
                    max=count
            if(x==')'):
                count-=1
        return max
