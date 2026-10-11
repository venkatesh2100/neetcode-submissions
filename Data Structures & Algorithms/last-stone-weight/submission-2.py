class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        n = len(stones)

        if n == 1:
            return stones[0]
        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)


            if x == y:
                continue 
            
            heapq.heappush(maxHeap , (x - (y)))

        
        return -maxHeap[0] if maxHeap else 0