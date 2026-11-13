class Solution:
    def lowerbound___(self,nums: list[int], target):
        n=len(nums)
        low=0
        high=n-1
        lb=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def upperbound__(self,nums:list[int],target):
        n=len(nums)
        low=0
        high=n-1
        up=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                up=mid
                high=mid-1
            else:
                low=mid+1
        return up
   

    def searchRange(self, nums: list[int], target):
        IB=self.lowerbound___(nums, target)
        if IB == len(nums) or nums[IB] != target:
            return [-1,-1]
        UP=self.upperbound__(nums,target)

        return [IB,UP-1]
       
        