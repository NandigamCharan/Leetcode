import math

def decode(i):
    return i % n

def is_equal(a, b, start):
    j = start
    for i in range(0, k):
        if a[decode(j)] != b[i]:
            return False
        j += 1
    return True

def hash_of_b(b):
    h = 0
    for i in b:
        h = (((h + prime) * basenum) + ord(i)) % prime
    return (h + prime) % prime

def hash_of_a(a):
    h = 0
    i = 0
    while i < k:
        h = (((h + prime) * basenum) + ord(a[decode(i)]))% prime
        i += 1
    return (h + prime) % prime

def offset_of(k):
    k = k - 1
    off = 1
    for i in range(k):
        off = (off * basenum)% prime
    return off

def rhash(h, old, new):
    return ((h + prime - ord(old) * offset) * basenum + ord(new)) % prime

def stringmatch(a,b):

    global k; k = len(b)            # These are global variables
    global n; n = len(a)
    global prime; prime = 101       # prime for hashing,
    global basenum; basenum = 128   # primes
    global offset; offset = offset_of(k)  # This is the offset bits for hash function
    hash_b = hash_of_b(b)
    rolling_hash = hash_of_a(a)

    for i in range(n):
        if rolling_hash == hash_b and is_equal(a, b, i):
                return math.ceil((i + k) / n)
        rolling_hash = rhash(rolling_hash, a[decode(i)], a[decode(i + k)])
    return -1