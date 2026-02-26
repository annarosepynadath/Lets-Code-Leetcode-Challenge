class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        for x in nums:
            if(x%3==0) and (x%2==0):
                sum+=x
                count+=1
        if (count==0):
            return 0
        else:
            return int(sum/count)
