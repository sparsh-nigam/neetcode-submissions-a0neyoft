class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #solved with array and its optimal solution as space complexity O(1) dict has O(n)
        freq=[0]*26
        left=0
        max_freq=0
        max_length=0

        for right in range(len(s)):
            ch=s[right]
            #character ko index me convert
            idx=ord(ch)-ord('A')
            freq[idx]+=1
            max_freq=max(max_freq,freq[idx])

            window=right-left+1
            if window-max_freq>k:
                left_idx=ord(s[left])-ord('A')
                freq[left_idx]-=1
                left+=1
            window =right-left+1
            max_length=max(max_length,window)
        return max_length
