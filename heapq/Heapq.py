import heapq
import random

heap = []
heapq.heapify(heap)
for i in range(15):
    item = random.randint(10, 100)
    print("coming ", item, end=' ')
    if len(heap) >= 5:
        top_item = heap[0] # smallest in heap
        if top_item < item: # min heap
            top_item = heapq.heappop(heap)
            print("pop", top_item, end=' ')
            heapq.heappush(heap, item)
            print("push", item, end=' ')
    else:
        heapq.heappush(heap, item)
        print("push", item, end=' ')
    pass
    print(heap)
pass

print("sort")
heap.sort()

print(heap)