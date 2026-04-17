class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        current_sum=nums[0]
        n=len(nums)

        for i in range(1,n):
            current_sum=current_sum+nums[i]
            if current_sum<nums[i]:
                current_sum=nums[i]
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum