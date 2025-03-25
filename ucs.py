# UCS Algorithm
def path_cost(path):
    total_cost = 0

    for (node, cost) in path:
        total_cost += cost
    return total_cost,path[-1][0]


def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)

        # last_tuple = path[-1]
        # node = last_tuple[0]

        node = path[-1][0]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path

        else:
            adjacent_nodes = graph.get(node, [])

            for tpl in adjacent_nodes:
                new_path = path.copy()
                new_path.append(tpl)

                queue.append(new_path)


def main():
    graph = {
        'S': [('A', 2), ('B', 3), ('D', 5)],
        'A': [('C', 4)],
        'B': [('D', 4)],
        'C': [('D', 1), ('G', 2)],
        'D': [('G', 5)],
        # 'G': []
    }

    solution = ucs(graph, 'S', 'G')

    print(solution)
    print(path_cost(solution))


main()
