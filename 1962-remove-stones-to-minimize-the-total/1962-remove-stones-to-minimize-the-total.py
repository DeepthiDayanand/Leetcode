class Solution:
    import heapq
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [i * -1 for i in piles]
        heapq.heapify(piles)

        while k > 0:
            removed_stones = heapq.heappop(piles)
            heapq.heappush(piles, removed_stones//2)
            k -= 1
        
        return sum(piles)*-1