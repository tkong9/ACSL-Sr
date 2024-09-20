import heapq

'''
Priority Queue
Priority Queue is an extension of queue with following properties.
1. Every item has a priority associated with it.
2. An element with high priority is dequeued before an element with low priority.
3. If two elements have the same priority, they are served according to their order in the queue.
'''

# In python, heap is min heap by default
# To implement max heap, we can take the negative of the elements
# and then push them into the heap
# When we pop the element, we can take the negative of the element
# to get the original element

# Pushing elements into the heap

hq = []
heapq.heappush(hq, 3)
heapq.heappush(hq, 2)
heapq.heappush(hq, 8)
heapq.heappush(hq, 4)
heapq.heappush(hq, 10)
heapq.heappush(hq, 9)

# Pop and return the smallest element from the heap
print(heapq.heappop(hq))  # 2

# Pushing elements into the heap
heapq.heappush(hq, 5)
heapq.heappush(hq, 6)
heapq.heappush(hq, 7)
heapq.heappush(hq, -100)

# peek the smallest element from the heap
print(hq[0])  # -100

print(hq)  # [-100, 4, 7, 5, 10, 9, 8, 6]

# Priority Queue
new_heap = []

# Pushing elements into the heap
# You can push tuples with the first element as priority
# and the second element as the actual element
# The heap will be sorted based on the priority
# The first element in the tuple has higher priority than the second element
# You can also push tuples with more than 2 elements

heapq.heappush(new_heap, (1, 'A'))
heapq.heappush(new_heap, (2, 'B'))
heapq.heappush(new_heap, (3, 'C'))
heapq.heappush(new_heap, (4, 'A'))
heapq.heappush(new_heap, (4, 'B'))
heapq.heappush(new_heap, (1, 'B'))
heapq.heappush(new_heap, (4, 'C'))

print(heapq.heappop(new_heap))  # (1, 'A')
print(heapq.heappop(new_heap))  # (1, 'B')
print(heapq.heappop(new_heap))  # (2, 'B')
