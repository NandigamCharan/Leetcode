import string
import random

def prehash(b):
    prime = 101
    basenum = 128
    h = 0
    for i in b:
        h = (((h + prime) * basenum) + ord(i)) % prime
    return (h + prime) % prime

def presum(b):
    h = 0
    for i in b:
        h += ord(i)
    return h

test1 = set()
hash_collisions1 = 0

test2 = set()
hash_collisions2 = 0

n = 100
sample = 100000
for i in range(sample):
    x = ''.join(random.choices(string.ascii_lowercase + string.digits, k = n))
    h1 = prehash(x)
    if h1 in test1:
        hash_collisions1 += 1
    test1.add(h1)
    
    h2 = presum(x)
    if h2 in test2:
        hash_collisions2 += 1
    test2.add(h2)
test2 = list(test2)
test2.sort()

print("in test1 max = ",max(test1), "min = ", min(test1), "dif = ", max(test1) - min(test1))
print("in test2 max = ",max(test2), "min = ", min(test2), "dif = ", max(test2) - min(test2))
print(sample - hash_collisions1, sample - hash_collisions2)