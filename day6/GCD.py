class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        if(mx%mn==0):
            return mn
        for i in range(1,mn):
            if(mn%i==0 and mx%i==0):
                gcd=i
        return gcd
