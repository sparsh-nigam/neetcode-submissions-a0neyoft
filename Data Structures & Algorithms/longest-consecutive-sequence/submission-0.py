class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)        
        longest =0       #let assume longest length to be zero
        for num in num_set:
            if (num-1) not in num_set:
                num_length=1              #checking for start 

                while (num+num_length) in num_set:
                    num_length+=1

                longest=max(longest,num_length)
        return longest
