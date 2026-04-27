class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_dict={}
        s2_dict={}
        left=0
        for ch in s1:
            if ch in s1_dict:
                s1_dict[ch]+=1
            else:
                s1_dict[ch]=1
        #sliding window
        for right in range(len(s2)):
            ch=s2[right]
            if ch in s2_dict:
                s2_dict[ch]+=1
            else:
                s2_dict[ch]=1
#creating window
            if (right-left+1) > len(s1):
                left_char=s2[left]       #left character
                s2_dict[left_char]-=1    #frequency minus krdenge

                if s2_dict[left_char]==0:
                    del s2_dict[left_char]  #if frequency goes zero delete it from dict
                left+=1
            if s1_dict==s2_dict:
                return True
        return False


            