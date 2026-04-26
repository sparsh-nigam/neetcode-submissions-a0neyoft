class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_set=set()
        max_set=0
        left=0
        for i in range(len(s)):
            while s[i] in long_set:
                long_set.remove(s[left])
                left+=1
            long_set.add(s[i])    
            max_set=max(max_set,i-left+1)
        return max_set    