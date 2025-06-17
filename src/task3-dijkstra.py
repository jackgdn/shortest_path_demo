from ast import literal_eval

INF = float("inf")


def dijkstra(adjacency_list, start_node, node_count):
    distances = [INF] * node_count
    distances[start_node] = 0
    visited = [False] * node_count
    paths = [None] * node_count
    paths[start_node] = [start_node]

    for _ in range(node_count):
        min_distance = INF
        min_node = None
        for node in range(node_count):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is not None:
            visited[min_node] = True

        for u, w in adjacency_list[min_node]:
            if not visited[u] and distances[min_node] + w < distances[u]:
                distances[u] = distances[min_node] + w
                paths[u] = paths[min_node] + [u]

    return distances, paths


def main():
    with open("tasks\\task3.txt", "r") as task_file:
        data = task_file.read().strip().split("\n\n")
        raw_adjacency_list = literal_eval(data[0])
        mapping = literal_eval(data[1])

    adjacency_list = {
        mapping[u]: [(mapping[v], w) for v, w in raw_adjacency_list[u]]
        for u in raw_adjacency_list.keys()
    }

    node_count = len(adjacency_list)
    distances, paths = dijkstra(adjacency_list, mapping["A"], node_count)

    output_file = open("output\\task3-output.txt", "w")
    print("Dest\tDist\tPath")
    output_file.write("Dest\tDist\tPath\n")
    for node in range(node_count):
        print(
            f"{mapping[node]:<8}{distances[node]:<8}{'->'.join(map(lambda x: mapping[x], paths[node]))}"
        )
        output_file.write(
            f"{mapping[node]:<8}{distances[node]:<8}{'->'.join(map(lambda x: mapping[x], paths[node]))}\n"
        )
    output_file.close()


if __name__ == "__main__":
    main()
