class Solution:
    def trap(self, height: List[int]) -> int:
        #SOLVING WITH TWO POINTER
        h=height
        left=0
        right=len(h)-1

        left_max=0
        right_max=0

        trap_water = 0

        while left<right:
            if h[left]<h[right]:
                if h[left]>=left_max:
                    left_max=h[left]
                else:
                    trap_water+=left_max-h[left]
                left+=1
            else:
                if h[right]>=right_max:
                    right_max=h[right]
                else:
                    trap_water+=right_max-h[right]
                right-=1
        return trap_water
