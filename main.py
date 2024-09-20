from collections import deque
import time
import heapq

hq = []

# In python, heap is min heap by default

# Pushing elements into the heap
heapq.heappush(hq, 1)
heapq.heappush(hq, 2)
heapq.heappush(hq, 3)
heapq.heappush(hq, 4)

# Pop and return the smallest element from the heap
print(heapq.heappop(hq))  # 1

# Pushing elements into the heap
heapq.heappush(hq, 5)
heapq.heappush(hq, 6)
heapq.heappush(hq, 7)
heapq.heappush(hq, -100)


# peek the smallest element from the heap
print(hq[0])

print(hq)

# Priority Queue
new_heap = []

heapq.heappush(new_heap, (1, 'A'))
heapq.heappush(new_heap, (2, 'B'))
heapq.heappush(new_heap, (3, 'C'))
heapq.heappush(new_heap, (4, 'A'))
heapq.heappush(new_heap, (4, 'B'))
heapq.heappush(new_heap, (4, 'C'))
heapq.heappush(new_heap, (4, 'F'))
heapq.heappush(new_heap, (4, 'Z'))

print(heapq.heappop(new_heap))  # (1, 'A')
print(heapq.heappop(new_heap))  # (2, 'B')
print(heapq.heappop(new_heap))  # (3, 'C')
print(heapq.heappop(new_heap))  # (4, 'A')
print(heapq.heappop(new_heap))  # (4, 'B')
