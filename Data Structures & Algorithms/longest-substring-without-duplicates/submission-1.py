class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #without for loop
        long_set=set()
        left=0
        max_set=0
        i=0
        while i<len(s):
            if s[i] not in long_set:
                long_set.add(s[i])
                i+=1
                max_set=max(max_set,i-left)  #if i wrote i+=1 after this line then here it will be wriiten as i-left+1
            else:
                long_set.remove(s[left])
                left+=1
        return max_set                
        
