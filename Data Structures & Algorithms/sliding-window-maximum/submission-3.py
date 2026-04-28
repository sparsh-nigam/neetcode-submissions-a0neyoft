class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        num_list=[]
        left=0
        max_num=[]


        for right in range(len(nums)):
            num=nums[right]
            num_list.append(num)
            
            if len(num_list)==k:
                max_num.append(max(num_list))
                del num_list[left]
        return max_num

        # brute force tried but time limit exceed for large inputs