class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        minim=float("inf")

        while low<=high:
            mid=(low+high)//2

            if nums[mid]<=nums[high]:
                minim=min(minim,nums[mid])
                high=mid-1
            else:
                minim=min(minim,nums[low])
                low=mid+1
        return minim

            
       