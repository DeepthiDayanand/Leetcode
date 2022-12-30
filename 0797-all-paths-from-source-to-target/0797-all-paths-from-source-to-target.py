class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path)
                return
            for n in graph[node]:
                dfs(n, path + [n])

        dfs(0, [0])
        return ans

