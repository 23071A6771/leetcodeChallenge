class Solution:
    def twoSum(self, nums, target):
        seen = {}
        n=len(nums) 
        for i in range(n):
            rem=target-nums[i]
            if rem in seen:
                return [seen[rem],i]
            seen[nums[i]]=i

