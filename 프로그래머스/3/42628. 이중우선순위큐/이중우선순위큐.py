import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for op in operations:
        if op == "D 1":
            if len(min_heap) > 0 and len(max_heap) > 0:
                tmp = heapq.heappop(max_heap)[1]
                min_heap.remove(tmp)
            else:
                continue
        elif op == "D -1":
            if len(min_heap) > 0 and len(max_heap) > 0:
                tmp = heapq.heappop(min_heap)
                max_heap.remove((-tmp, tmp))
            else:
                continue
        else:
            real_num = int(op.replace("I ", ""))
            heapq.heappush(min_heap, real_num)
            heapq.heappush(max_heap, (-real_num, real_num))

    if len(min_heap) > 0 and len(max_heap) > 0:
        answer = [max_heap[0][1], min_heap[0]]
    else:
        answer = [0, 0]
    return answer