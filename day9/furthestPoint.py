class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist=0
        lcount=moves.count('L')
        rcount=moves.count('R')
        for i in moves:
            if(i=='L'):
                dist-=1
            elif(i=='R'):
                dist+=1
            elif(i=='_'):
                if(lcount>rcount):
                    dist-=1
                else:
                    dist+=1        
        if(dist<0):
            return dist*-1
        else:
            return dist
