class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:#complx: O(n log n)
        #USING IN-BUILT FUNCTIONS COUNTER MODULE
        from collections import Counter
        freq=Counter(nums)
        top_freq_k=freq.most_common(k)
        result=[]
        for num,count in top_freq_k:
            result.append(num)
        return result