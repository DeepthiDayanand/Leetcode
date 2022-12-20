class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visit, visited = set(), set()
        
        visit.add(0)
        while visit:
            curr = visit.pop()
            visited.add(curr)
            for room in rooms[curr]:
                if room not in visited:
                    visit.add(room)
        return len(visited) == len(rooms)