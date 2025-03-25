def path_h_cost(path):
    last_node = path[-1]

    h_cost = H_table[last_node]

    return h_cost, last_node


def greedy_best_search(graph, start, goal):
    visited = []
    queue = [[start]]

    while queue:
        queue.sort(key=path_h_cost)
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node)

            for node_1 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node_1)
                queue.append(new_path)


H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}


def main():
    graph = {
        'S': ['A', 'B'],
        'A': ['B', 'C', 'G'],
        'B': ['C'],
        'C': ['G']
    }

    solution = greedy_best_search(graph, 'S', 'G')

    print(solution)
    print(path_h_cost(solution))


if __name__ == "__main__":
    main()
