class Solution:
    def trap(self, height: List[int]) -> int:
        # Over Count
        curr_water = ans = 0
        curr_max = height[0]
        for h in height:
            if h >= curr_max:
                ans += curr_water
                curr_water = 0
                curr_max = h
            else:
                curr_water += curr_max - h
        ans += curr_water
        
        # Correct Over Counting
        i = len(height) - 1
        curr_min, curr_in = height[i], i
        correction = 0 
        while True:
            if height[i] >= curr_min:
                correction += (curr_max - curr_min) * (curr_in - i)
                curr_min, curr_in = height[i], i
            if height[i] == curr_max:
                break
            i -= 1
        return ans - correction