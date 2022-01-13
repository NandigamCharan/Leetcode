class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        K = nums[0]
        n = len(nums)
        prev = 0
        for i in range(1, n):
            s = K[i - 1] + nums[i]
            if s > nums[i]:
                K.append(s)
            else:
                K.append(nums[i])
        return max(K)