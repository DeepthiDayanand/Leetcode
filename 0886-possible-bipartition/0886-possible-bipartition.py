#BFS Solution

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for  a, b in dislikes:
            adjacency_list[a - 1].append(b - 1)
            adjacency_list[b - 1].append(a - 1)
            
        colours = [0]*n  #not visited 0, a = 1, b = 2
        
        for start in range(n):
            if colours[start] == 0:
                queue = deque([start])
                colours[start] = 1
                
                while queue:
                    v = queue.popleft()
                    for neighbour in adjacency_list[v]:
                        if colours[neighbour] == 0:
                            colours[neighbour] = 3 - colours[v]
                            queue.append(neighbour)
                        elif colours[neighbour] == colours[v]:
                            return False
                        
        return True
        