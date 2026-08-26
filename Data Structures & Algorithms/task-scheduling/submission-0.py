class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-c for c in task_count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque() # stores count and idle time

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(max_heap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
