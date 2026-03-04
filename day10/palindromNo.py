class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        n=x
        y=0
        while n!=0:
            y=y*10+n%10
            n=n//10
        if(y==x):
            return True
        else:
            return False
