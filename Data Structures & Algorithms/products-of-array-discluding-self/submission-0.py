class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        #core concept get prefix then suffix then(prefix*suffix)
        #For Prefix
        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        #For suffix then suffix multiplied by prefix stored in res
        suffix=1
        for i in range(n-1,-1,-1):  #from right to left
            res[i]*=suffix          
            suffix*=nums[i]
        return res
