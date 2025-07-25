from ast import literal_eval
from pathlib import Path

INF = float("inf")


def floyd(adjacency_matrix, node_count):
    distances = [
        [adjacency_matrix[i][j] for j in range(node_count)] for i in range(node_count)
    ]
    paths = [
        [[i] if i == j else [i, j] for j in range(node_count)]
        for i in range(node_count)
    ]

    for u in range(node_count):
        for p in range(node_count):
            if distances[u][p] == INF:
                continue
            for v in range(node_count):
                if distances[p][v] == INF:
                    continue

                if distances[u][p] + distances[p][v] < distances[u][v]:
                    distances[u][v] = distances[u][p] + distances[p][v]
                    paths[u][v] = paths[u][p][:-1] + paths[p][v]

    return distances, paths


def main():
    task_file_path = Path(__file__).parent.parent / Path("tasks") / "task4.txt"
    with open(task_file_path, "r") as task_file:
        adjacency_list = literal_eval(task_file.read())
        node_count = len(adjacency_list)

    adjacency_matrix = [
        [next((w for v, w in sorted(pairs) if v == j), INF) for j in range(node_count)]
        for _, pairs in sorted(adjacency_list.items())
    ]

    distances, paths = floyd(adjacency_matrix, node_count)
    result = sorted(
        [(u, v) for u in range(node_count) for v in range(node_count) if u != v],
        key=lambda x: (distances[x[0]][x[1]], len(paths[x[0]][x[1]]), x[0], x[1]),
    )

    output_file_path = (
        Path(__file__).parent.parent / Path("output") / "task4-output.txt"
    )
    output_file = open(output_file_path, "w")
    print("Srce\tDest\tDist\tPath")
    output_file.write("Srce\tDest\tDist\tPath\n")
    for u, v in result:
        if distances[u][v] == INF:
            print(f"{'s' + str(u + 1):<8}{'s' + str(v + 1):<8}{INF:<8}{None}")
            output_file.write(
                f"{'s' + str(u + 1):<8}{'s' + str(v + 1):<8}{INF:<8}{None}\n"
            )
        else:
            print(
                f"{'s' + str(u + 1):<8}{'s' + str(v + 1):<8}{distances[u][v]:<8}{'->'.join(map(lambda x: 's' + str(x + 1), paths[u][v]))}"
            )
            output_file.write(
                f"{'s' + str(u + 1):<8}{'s' + str(v + 1):<8}{distances[u][v]:<8}{'->'.join(map(lambda x: 's' + str(x + 1), paths[u][v]))}\n"
            )
    output_file.close()


if __name__ == "__main__":
    main()
