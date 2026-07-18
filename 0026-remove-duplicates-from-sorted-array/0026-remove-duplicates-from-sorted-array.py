class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        n=len(nums)
        i=0
        j=i+1
        while i<n and j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1