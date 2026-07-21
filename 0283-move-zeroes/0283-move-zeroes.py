class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        start=0
        for i in range(0,n):
            if nums[i]!=0:
                nums[i],nums[start]=nums[start],nums[i]
                start+=1