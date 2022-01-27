from sortedcontainers import SortedList

def lis(nums):
    S = SortedList()
    for i in nums:
        if len(S) != 0 and S[-1] > i:
            x = S.bisect_left(i)
            S.remove(S[x])
        S.add(i)
    return len(S)