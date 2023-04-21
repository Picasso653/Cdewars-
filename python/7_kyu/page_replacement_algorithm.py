def fifo(n, ref):
    queue = [-1 for k in range(n)]
    j = 0
    if ref == []:
        return queue
    for i in ref:
        if len(queue)>= n:
            if i not in queue:
                queue[j%n] = i
                j += 1
        elif i not in queue:
            queue.append(i)
    return queue
            