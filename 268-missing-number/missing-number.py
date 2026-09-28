class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sum=0

        for i in range(0,n):
            sum+=nums[i]

        return (n*(n+1))//2-sum



        
            
        