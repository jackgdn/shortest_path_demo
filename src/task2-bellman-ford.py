from ast import literal_eval

INF = float("inf")


def bellman_ford(adjacency_matrix, start_node, node_count):
    distances = [INF] * node_count
    distances[start_node] = 0
    paths = [None] * node_count
    paths[start_node] = [start_node]

    for _ in range(node_count - 1):
        for u in range(node_count):
            for v in range(node_count):
                w = adjacency_matrix[u][v]
                if distances[u] != INF and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    paths[v] = paths[u] + [v]

    return distances, paths


def main():
    with open("tasks\\task1.txt", "r") as task_file:
        adjacency_matrix = [
            [INF if isinstance(x, str) else x for x in row]
            for row in literal_eval(task_file.read())
        ]

    node_count = len(adjacency_matrix)
    distances, paths = bellman_ford(adjacency_matrix, 0, node_count)

    result = tuple(zip(distances, paths))
    output_file = open("output\\task2-output.txt", "w")
    print("Dest\tDist\tPath")
    output_file.write("Dest\tDist\tPath\n")
    for node in range(node_count):
        print(
            f"{'C' + str(node + 1):<8}{result[node][0]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), result[node][1]))}"
        )
        output_file.write(
            f"{'C' + str(node + 1):<8}{result[node][0]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), result[node][1]))}\n"
        )
    output_file.close()


if __name__ == "__main__":
    main()
