class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #SOLVED USING DICTIONARY
        freq={}
        left=0
        max_freq=0
        max_length=0

        for right in range(len(s)):
            char=s[right]
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
            max_freq=max(max_freq,freq[char])
            window=right-left +1
            if window-max_freq>k:
                freq[s[left]]-=1
                left+=1
            #window = right-left+1
            max_length=max(max_length,right-left+1)  #window (is updated so we need to write it again)
        return max_length
