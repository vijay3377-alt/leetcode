class Solution(object):
    def remainingMethods(self,n,k,invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph=[[] for _ in range(n)]
        for a,b in invocations:
            graph[a].append(b)
        suspicious = set()
        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)
        dfs(k)
        for a,b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        ans=[]
        for i in range(n):
            if i not in suspicious:
                ans.append(i)
        return ans
        