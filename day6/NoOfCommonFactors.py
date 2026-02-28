class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        if(a>b):
            temp=a
            a=b
            b=temp

        for i in range(1,a+1):
            if(a%i==0 and b%i==0):
                count+=1
        return count
