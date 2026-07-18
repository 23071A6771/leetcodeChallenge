class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            sum=-1*nums[i]
            while l<r:
                s=nums[l]+nums[r]
                if sum==s:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<n and nums[l]==nums[l-1]:
                        l+=1
                    while r>=0 and nums[r]==nums[r+1]:
                        r-=1
                elif sum>s:
                    l+=1
                else:
                    r-=1
        return res

        