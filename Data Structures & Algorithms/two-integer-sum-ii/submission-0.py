class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0          #--> Start from left
        j=n-1        #--> Start from right

        while i<j:   #Two pointer loop move i from left and j from right
            total=numbers[i]+numbers[j]
            if total==target:
                return [i+1,j+1]
            elif total<target:
                i+=1
            elif total>target:     # we can simply write 'else' also 
                j-=1