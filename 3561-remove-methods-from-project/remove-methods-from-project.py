class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        suspicious = [False] * n
        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)
        dfs(k)
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i]]