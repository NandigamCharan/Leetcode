
def findMinHealth(power, armor):
    m = max(power)
    s = sum(power) + 1
    return s - armor if m >= armor else s - m


def findMinHealth(power, armor):
    return sum(power) - min(armor, max(power)) + 1


# def findMinHealth(power, armor):
#     state = float("inf")
#     for p in power:
#         if abs(armor - p) < abs(armor - state):
#             state = p
#     return sum(power) - armor + max(armor - state, 0) + 1


p = [1,2,3]
a = 4
print(findMinHealth(p, a))










# def minimumGroups(awards, k):
#     awards.sort()
#     # print(awards , k)
#     starter = awards[0]
#     count = 1
#     for i in awards:
#         # print(starter, i)
#         if i - starter > k:
#             starter = i
#             count += 1
#     return count



# A = [3, 1, 4, 3, 9, 10]
# k = 10
# A = [1, 13, 6, 8, 9, 3, 5]
# k = 4
# A = [1,5,4,6,8,9,2]
# k = 3
# print(minimumGroups(A, k))