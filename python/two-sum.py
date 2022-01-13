class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i, data in enumerate(nums):
            if data in H:
                return [H[data], i]
            else:
                H[target - data] = i