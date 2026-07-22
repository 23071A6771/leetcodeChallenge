class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        n=len(nums)

        for i in range(0,n):
            if nums[i] in set1:
                return True
            set1.add(nums[i])
        
        return False