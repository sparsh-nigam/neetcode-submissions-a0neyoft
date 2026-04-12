class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#USING HASH SET
        numsset=set()

        for i in nums:
            if i in numsset:
                return True
            numsset.add(i)
        return False