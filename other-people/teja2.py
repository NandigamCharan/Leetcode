import re


def firstIndex(arr, x):
    def findit(arr, i, x):
        if i >= len(arr):
            return -1
        if arr[i] == x:
            return i
        return findit(arr, i+1, x)
    return findit(arr, 0, x)


def firstIndex(arr, x, i=0):
    if i >= len(arr):
        return -1
    if arr[i] == x:
        return i 
    return firstIndex(arr, x, i + 1)

def lastIndex(arr, x):
    def findit(arr, i, x):
        if i < 0:
            return -1
        if arr[i] == x:
            return i
        return findit(arr, i-1, x)
    return findit(arr, len(arr)-1, x)

def lastIndex(arr, x):
    def findit(arr, ans, i , x):
        if i >= len(arr):
            return ans
        if arr[i] == x:
            return findit(arr, i, i + 1, x)
        return findit(arr, ans, i + 1, x)
    return findit(arr, -1,  0, x)


def lastIndex(arr, x, i=0, ans=-1):
    if i >= len(arr):
        return ans
    if arr[i] == x:
        return lastIndex(arr, x, i+1, i)
    return lastIndex(arr, x, i+1, ans)



