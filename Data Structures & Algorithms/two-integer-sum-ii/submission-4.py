class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #USING HASMAP CONCEPT
        index={}
        for i in range(len(numbers)):
            seen = target - numbers[i]
            if seen in index:
                return[index[seen]+1,i+1]
            index[numbers[i]]=i