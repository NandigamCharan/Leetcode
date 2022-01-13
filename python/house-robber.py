class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i):
            if i in D:
                return D[i]
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            if i == len(nums) - 2:
                return max(nums[i], nums[i + 1])
            D[i] = nums[i] + max(recurse(i + 2), recurse(i + 3))
            return D[i]
        D = {}
        ans = max(recurse(0), recurse(1))
        return ans 