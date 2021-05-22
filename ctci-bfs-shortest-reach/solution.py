class Graph(object):

    def __init__(self, n):
        self.num_nodes = n
        self.adjacent = [[] for i in range(n)]

    def connect(self, i, j):
        self.adjacent[i].append(j)
        self.adjacent[j].append(i)

    def find_all_distances(self, start):
        dist = [-1] * self.num_nodes
        dist[start] = 0

        to_visit = [(start, i) for i in self.adjacent[start]]
        visited = set([start])

        while len(to_visit) != 0:
            from_, to = to_visit.pop(0)

            if to in visited:
                continue
            visited.add(to)

            dist[to] = dist[from_] + 6

            for i in self.adjacent[to]:
                to_visit.append((to, i))

        del dist[start]
        print(' '.join(map(lambda n: str(n), dist)))


if __name__ == '__main__':
    t = input()
    for i in range(t):
        n,m = [int(x) for x in raw_input().split()]
        graph = Graph(n)
        for i in xrange(m):
            x,y = [int(x) for x in raw_input().split()]
            graph.connect(x-1,y-1)
        s = input()
        graph.find_all_distances(s-1)
