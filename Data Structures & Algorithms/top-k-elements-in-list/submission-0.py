class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #complexity O(n) using bucket sort
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
#creating bucket
        bucket=[]
        for i in range(len(nums)+1):  #--> we can write it in shorter way also
                                      # bucket=[[] for i in range(len(nums)+1)]
            bucket.append([])         #it works same
        
#filling bucket
        for num,freq in count.items():
            bucket[freq].append(num)

        result=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
               result.append(num)
               if len(result)==k:
                   return result