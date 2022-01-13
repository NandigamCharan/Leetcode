class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        n = len(nums) - 1
        moves = nums[0]
        for i in range(1,n):
            if nums[i] == 0 and moves == 1:
                    return False
            moves = max(moves - 1 ,nums[i])
        return True  

