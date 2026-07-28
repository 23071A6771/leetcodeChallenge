class Solution:
    def findpow(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        a=self.findpow(x,n//2)
        if n%2==1:
            return a*a*x
        else:
            return a*a  
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.findpow(x,n)
        else:
            n*=-1
            return 1/self.findpow(x,n)
        