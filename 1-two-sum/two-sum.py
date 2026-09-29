class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)

        freq={}

        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in freq:
                return [freq[remaining],i]

            freq[nums[i]]=i
            
        


    