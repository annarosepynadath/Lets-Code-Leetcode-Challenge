import math
class Solution:
    def isThree(self, n: int) -> bool:
        if(n==1):
            return False
        root=int(math.sqrt(n))
        if(n!=root*root):
            return False
        for i in range(2,int(math.sqrt(root))+1):
            if(root%i==0):
                return False
        return True
