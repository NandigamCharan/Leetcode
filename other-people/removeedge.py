from queue import Queue

G = {}
n = int(input())
for i in range(n):
    x = input()
    G[x] = []

e = int(input())
for i in range(e):
    x = input().split(" ")
    G[x[0]].append(x[1])

x = input()
y = input()

vis = set()
ans = []
q = Queue()
vis.add(x)
ans = []
q = Queue()
vis.add(x)
q.put(x)
print()
while not q.empty():
    a = q.get()
    print(a)
    for i in G[a]:
        if i not in vis:
            if i == y:
                print(a)
                ans.append(a)
            else:
                vis.add(i)
                q.put(i)
ans.sort()
print("ans")
print(*ans, sep=" ")
