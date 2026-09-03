class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if (self.minHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]) or (len(self.maxHeap) - len(self.minHeap) > 1):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

    def findMedian(self) -> float:

        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2

        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        else:
            return -self.maxHeap[0]
        