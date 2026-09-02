from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        que = deque()
        heapq.heapify(maxHeap)

        cycles = 0
        while maxHeap or que:
            if que and que[0][1] == cycles:
                heapq.heappush(maxHeap, que[0][0])
                que.popleft()

            if maxHeap:
                cnt = heapq.heappop(maxHeap)

                if cnt + 1 !=0:
                    que.append([cnt + 1, cycles + n + 1])

                cnt += 1
            

            

            cycles += 1

        return cycles

