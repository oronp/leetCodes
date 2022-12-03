from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        nodes_dict = {e:[] for e in range(n)}
        for edge in edges:
            current, neighbor = edge[0], edge[1]
            nodes_dict[current].append(neighbor)
            nodes_dict[neighbor].append(current)
        return BFS_like(source, destination,nodes_dict)

def BFS_like(source, dest, nodes):
    visited = [source]
    burned = []
    while len(visited):
        if visited[0] not in burned:
            visited.extend(nodes[visited[0]])
            burned.append(visited.pop(0))
            if dest in visited:
                return True
        else:
            visited.pop(0)
    return False


solution = Solution
print(solution.validPath(self=solution, n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, destination=5))