from ast import literal_eval
from pathlib import Path

INF = float("inf")


def dijkstra(adjacency_matrix, start_node, node_count):
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

        for next_node, next_distance in enumerate(adjacency_matrix[min_node]):
            if (
                not visited[next_node]
                and distances[min_node] + next_distance < distances[next_node]
            ):
                distances[next_node] = distances[min_node] + next_distance
                paths[next_node] = paths[min_node] + [next_node]

    return distances, paths


def main():
    task_file_path = Path(__file__).parent.parent / Path("tasks") / "task1.txt"
    with open(task_file_path, "r") as task_file:
        adjacency_matrix = [
            [INF if isinstance(x, str) else x for x in row]
            for row in literal_eval(task_file.read())
        ]

    node_count = len(adjacency_matrix)
    distances, paths = dijkstra(adjacency_matrix, 0, node_count)

    output_file_path = (
        Path(__file__).parent.parent / Path("output") / "task1-output.txt"
    )
    output_file = open(output_file_path, "w")
    print("Dest\tDist\tPath")
    output_file.write("Dest\tDist\tPath\n")
    for node in range(node_count):
        print(
            f"{'C' + str(node + 1):<8}{distances[node]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), paths[node]))}"
        )
        output_file.write(
            f"{'C' + str(node + 1):<8}{distances[node]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), paths[node]))}\n"
        )
    output_file.close()


if __name__ == "__main__":
    main()
