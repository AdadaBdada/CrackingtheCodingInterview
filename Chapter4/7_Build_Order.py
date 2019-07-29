import collections


def buildOrder(projects, dependencies):
    graph = {u: [] for u in projects}
    incomEdge = collections.defaultdict(list)

    for u, v in dependencies:
        graph[u].append(v)
        incomEdge[v].append(u)

    queue = collections.deque([node for node in projects if not incomEdge[node]])
    count = 0
    buildOrder = []

    while queue:

        node = queue.popleft()
        buildOrder.append(node)
        count += 1

        for depend in graph[node]:
            incomEdge[depend].remove(node)  # remove incoming edges

            if not incomEdge[depend]:
                queue.append(depend)

    if count == len(projects):
        return buildOrder
    else:
        return []


if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

    order = buildOrder(projects, dependencies)
    print(order)
