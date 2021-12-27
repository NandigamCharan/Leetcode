import math

def decode(i):
    return i % n

def isequal(a, b, start):
    j = start
    for i in range(0, k):
        if a[decode(j)] != b[i]:
            return False
        j += 1
    return True

def hash_of_b(b):
    h = 0
    for i in b:
        h = (((h ) * basenum) + ord(i)) % prime
    return (h + prime) % prime

def hash_of_a(a):
    h = 0
    i = 0
    while i < k:
        h = (((h) * basenum) + ord(a[decode(i)]))% prime
        i += 1
    return h

def offsetof(k):
    k = k - 1
    off = 1
    for i in range(k):
        off = (off * basenum)% prime
    return off

def rhash(h, old, new):
    return ((h + prime - ord(old) * offset) * basenum + ord(new)) % prime

def stringmatch(a,b):

    global k; k = len(b)    # These are global variables
    global n; n = len(a)
    global prime; prime = 101 # prime for hashing,
    global basenum; basenum = 256
    global offset; offset = offsetof(k)  # This is the offset bits for hash function
    bhash = hash_of_b(b)
    h = hash_of_a(a)

    for i in range(n):
        if h == bhash and isequal(a, b, i):
                return math.ceil((i + k) / n)
        h = rhash(h, a[decode(i)], a[decode(i + k)])
    return -1