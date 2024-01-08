import random

def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            data = list(map(int, line.split()))
            vertex = data[0]
            neighbors = data[1:]
            graph[vertex] = neighbors
    return graph

def karger_min_cut(graph):
    while len(graph) > 2:
        # Choose a random edge
        vertex1 = random.choice(list(graph.keys()))
        vertex2 = random.choice(graph[vertex1])

        # Combine the neighbors of vertex2 with vertex1
        graph[vertex1].extend(graph[vertex2])
        for neighbor in graph[vertex2]:
            graph[neighbor].remove(vertex2)
            graph[neighbor].append(vertex1)

        # Remove self-loops (vertex pointing to itself)
        graph[vertex1] = [neighbor for neighbor in graph[vertex1] if neighbor != vertex1]

        # Delete the row containing vertex2
        del graph[vertex2]

    # Return the number of edges between the last 2 vertices
    return len(graph[list(graph.keys())[0]])

def run_multiple_tests(file_path, num_tests):
    min_cut_result = float('inf')
    for _ in range(num_tests):
        graph = read_graph(file_path)
        min_cut = karger_min_cut(graph)
        if min_cut < min_cut_result:
            min_cut_result = min_cut
    return min_cut_result

# Example usage:
file_path = "input.txt"  # The path of your file text
num_tests = 100
min_cut = run_multiple_tests(file_path, num_tests)
print(f"The minimum cut over {num_tests} trials is:", min_cut)
