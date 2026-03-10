class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=1
        for i in range(2,int(math.sqrt(num)+1)):
            if(num%i==0):
                sum+=i
                print(sum)
                sum+=(num/i)
                print(sum)
        print(sum)
        if(sum==1):
            return False
        if(sum==num):
            return True
        else:
            return False
