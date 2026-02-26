class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sum=0
        count=0
        n=len(nums)
        for i in range (n):
            sum+=nums[i]
            if(sum==0):
                count+=1
        return count
