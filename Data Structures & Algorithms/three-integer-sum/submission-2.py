class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        for i in range(n-2):   #we can write (n-2) also instead of n because last 2 indeces are of no use 
            j=i+1
            k=n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if nums[j]+nums[k]==-nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[j]+nums[k]>-nums[i]:
                    k-=1
                elif nums[j]+nums[k]<-nums[i]:
                    j+=1
        return res