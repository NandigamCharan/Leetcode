class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarysearch(A, i, j, t):
            if i <= j:
                mid = j + i >> 1
                if A[mid] == t:
                    return mid
                elif A[mid] > t:
                    return binarysearch(A, i, mid - 1, t)
                else:
                    return binarysearch(A, mid + 1, j, t)
            else:
                return -1

        def findpiv(A):
            def min_index(A, i, n):
                m = A[i]
                index = i
                while i <= n:
                    if A[i] < m:
                        m = A[i]
                        index = i
                    i += 1
                return index
            
            n = len(A)
            i = 0
            while True:
                if i >= n:
                    return 0
                x = 2 * (i + 1) - 1
                next = x if x < n else n - 1
                if A[i] > A[next]:
                    return min_index(A, i, next)
                i = x
        piv = findpiv(nums)
        a = binarysearch(nums, 0, piv-1, target)
        if a != -1:
            return a
        return binarysearch(nums,piv, len(nums)-1, target) 
        