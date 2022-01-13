from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        C = {}
        def colorit(node, color):
            C[node] = color
            status = True
            for i in graph[node]:
                if i not in C:
                    status = colorit(i, not(color))
                elif C[i] == C[node]:
                    status = False
                if not status:
                    return False
            return True
        for i in range(len(graph)):
            if i not in C:
                a = colorit(i, True)
                if not a:
                    return False
        return True