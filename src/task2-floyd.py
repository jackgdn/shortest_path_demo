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
    task_file_path = Path("tasks") / "task1.txt"
    with open(task_file_path, "r") as task_file:
        adjacency_matrix = [
            [INF if isinstance(x, str) else x for x in row]
            for row in literal_eval(task_file.read())
        ]

    node_count = len(adjacency_matrix)
    distances, paths = floyd(adjacency_matrix, node_count)

    output_file_path = Path("output") / "task2-output.txt"
    output_file = open(output_file_path, "w")
    print("Dest\tDist\tPath")
    output_file.write("Dest\tDist\tPath\n")
    for node in range(node_count):
        print(
            f"{'C' + str(node + 1):<8}{distances[0][node]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), paths[0][node]))}"
        )
        output_file.write(
            f"{'C' + str(node + 1):<8}{distances[0][node]:<8}{'->'.join(map(lambda x: 'C' + str(x + 1), paths[0][node]))}\n"
        )
    output_file.close()


if __name__ == "__main__":
    main()
