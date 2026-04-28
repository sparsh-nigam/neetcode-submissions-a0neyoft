class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        s_freq={}
        t_freq={}
        left=0
        formed=0   #means all t_freq exist in s_frequecy
        min_length=float("inf")
        min_window=""

        for ch in t:
            if ch in t_freq:
                t_freq[ch]+=1
            else:
                t_freq[ch]=1
        required=len(t_freq)
        for right in range(len(s)):
            ch=s[right]
            if ch in s_freq:
                s_freq[ch]+=1
            else:
                s_freq[ch]=1
            
            if ch in t_freq and s_freq[ch]==t_freq[ch]:
                formed+=1
            #SHRINK WINDOW IF CONDITION MET 
            while formed==required:  #condition met
                if right-left+1<min_length:
                    min_length=right-left+1
                    min_window=s[left:right+1]
                left_char=s[left]
                s_freq[left_char]-=1

                if left_char in t_freq and s_freq[left_char]<t_freq[left_char]:
                    formed-=1
                left+=1
        return min_window