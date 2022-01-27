# # 21 1275
# # 24 ic 

# #Done write yet
# # Try, if it does work undo...
# # change that function./. not every thing...


# def left_rotation(l1, n):
#     return l1[n:] + l1[:n] 




# def isPrime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     root = int(n ** (0.5) + 1)
#     for i in range(2, root):
#         if n % i == 0:
#             return False
#     return True

# def closeprime(n):
#     i = 0
#     while True:
#         if isPrime(n + i):
#             return n + i
#         if isPrime(n - i):
#             return n - i
#         i += 1

# n = int(input())
# print(closeprime(n))






def iscol(s, girl, n):
    c = 0
    for j in range(n):
        if s[j][girl] == 1:
            c += 1
        if c == 2:
            return False
    return True

def collison(s, n, m):
    count = 0
    for i in range(m):
        if not iscol(s, i, n):
            count += 1
    return count

A = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0]
]
print(collison(A, 3, 3))