def answer(A):
    def find(i):
        c = 0
        while i % 2 == 0:
            i //= 2
            c += 1
        if i == 1:
            return c
        k = 1
        while k < i:
            k = k << 1
        print(k)
        return count + int(k  + 1** (0.5))
    count = 0
    for i in A:
        x = find(i)
        print(i, x)
        count += x
    return count



A = [1]
A = [5, 8]
print(answer(A))