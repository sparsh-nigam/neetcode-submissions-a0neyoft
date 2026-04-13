class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: #complexity O(nlogn)
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sort_freq=sorted(freq.items(),key=lambda x:x[1])

        result=[]
        top_freq_k=sort_freq[-k:]
        for pair in top_freq_k:
            result.append(pair[0])
        return result

