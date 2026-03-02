class Solution:
    def judgeCircle(self, moves: str) -> bool:
        (x,y)=(0,0)
        for i in moves:
            if(i=='L'):
                (x,y)=(x-1,y)
            elif(i=='R'):
                (x,y)=(x+1,y)
            elif(i=='U'):
                (x,y)=(x,y+1)
            elif(i=='D'):
                (x,y)=(x,y-1)
        if((x,y)==(0,0)):
            return True
        else:
            return False
        
