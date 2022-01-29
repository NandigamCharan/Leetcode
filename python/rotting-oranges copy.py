from collections import deque as que

def answer(grid):
    def find_rotten(grid):              # This finds all the rotten oranges
        A = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    A.append((i, j))
        return A

    def in_bound(i, j):                 # check if i in bound or not
        if i >= 0 and j >= 0 and i < m and j < n:
            return True
        return False
    def neighbors(i,j):                 # gives all the vaild neighbors
        n = []
        if in_bound(i-1,j): n.append(i-1,j)
        if in_bound(i,j-1): n.append(i,j-1) 
        if in_bound(i+1,j): n.append(i+1,j)
        if in_bound(i,j+1): n.append(i,j+1)
        return n
    
    """
    The idea is move, layer by layer... from all rotten cells... count # of layers before queue gets emptied
    Same ideas as normal BFS, but here we are doing BFS  with multiple nodes
    """
    
    m = len(grid)
    n = len(grid[0])
    q = que()
    q.append((find_rotten(grid)))
    
    count = 0
    while True:
        nodes = q.popleft()              # removes front
        A = []                           # nodes in the next layer nodes
        for i, j in nodes:
            for x, y in neighbors(i,j):
                if grid[x][y] == 1:      # if not visited : mark as visited, and add to next layer
                    grid[x][y] = 2
                    A.append((x,y))
        if A == []:                      # if nothing to visited next : break. BREAK CONDITION
            break
        q.append(A)                      # add which nodes to vist next to queue
        count += 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    return count








    # q = Queue()
    # q.put(find_rotten(grid))
    # count = 0
    # while q.empty():
    #     nodes =  q.get()
    #     A = []
    #     for i, j in nodes:
    #         for x, y in neighbors(i,j):
    #             if grid[x][y] != 2:
    #                 grid[i][j] = 2
    #                 A.append(x,y)
    #     if A != []:
    #         q.put(A)
    #     count += 1
    
    # m = len(grid)
    # n = len(grid[0])
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] != 3:
    #             return -1
    # return count