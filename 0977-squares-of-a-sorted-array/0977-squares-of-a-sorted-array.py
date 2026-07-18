class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        res=[]
        for i in range(0,len(nums)):
            if nums[i]>=0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        n=len(a)
        m=len(b)
        for i in range(0,m):
            b[i]=b[i]*b[i]
        b.reverse()
        for i in range(0,n):
            a[i]=a[i]*a[i]
        i=0
        j=0
        while i<n and j<m:
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            elif a[i]>b[j]:
                res.append(b[j])
                j+=1
            else:
                res.append(a[i])
                res.append(b[j])
                i+=1
                j+=1
        while j<m:
            res.append(b[j])
            j+=1
        while i<n:
            res.append(a[i])
            i+=1
        return res

        
        

        