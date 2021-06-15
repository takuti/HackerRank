n = int(raw_input())

queue = []

for _ in range(n):
    query = list(map(int, raw_input().split(' ')))
    if query[0] == 1:  # enqueue
        queue.append(query[1])
    elif query[0] == 2:
        queue.pop(0)
    else:
        print(queue[0])
