class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate



from random import randint

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        def count(x):
            c = 0
            for i in nums:
                if i == x:
                    c += 1
            return c
        def recurse():
            i = randint(0, n)
            if count(nums[i]) > n // 2:
                return nums[i]
            return recurse()
        return recurse()