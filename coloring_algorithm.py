import random

def initialize_graph(num_nodes, edges):
    graph = {i: set() for i in range(num_nodes)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph

def get_max_degree(graph):
    max_degree = 0

    for neighbors in graph.values():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree

    return max_degree


def get_available_colors(neighbors, colored_nodes, max_degree):
    used_colors = set()
    available_colors = []

    for neighbor in neighbors:
        if neighbor in colored_nodes:
            used_colors.add(colored_nodes[neighbor])
    
    for color in range(max_degree + 1):
        if color not in used_colors:
            available_colors.append(color)
    return available_colors
    
def color_graph(graph):
    max_degree = get_max_degree(graph)
    colored_nodes = {}
    uncolored_nodes = set(graph.keys())

    while uncolored_nodes:
        candidate_colors = {}

        for node in uncolored_nodes:
            available_colors = get_available_colors(graph[node], colored_nodes, max_degree)
            candidate_colors[node] = random.choice(available_colors)

        for node in uncolored_nodes.copy():
            neighbor_colors = [candidate_colors[neighbor] for neighbor in graph[node] if neighbor in candidate_colors]
            if candidate_colors[node] not in neighbor_colors:
                colored_nodes[node] = candidate_colors[node]
                uncolored_nodes.remove(node)

    return colored_nodes


# small test set
print("Small test-set:")
graph = initialize_graph(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
colored_nodes = color_graph(graph)

for node, color in sorted(colored_nodes.items()):
    print(f"Node {node} has color {color}")

# large test set
print("Large test-set:")
num_nodes = 200
edges = [(i, i + 1) for i in range(num_nodes - 1)]

large_graph = initialize_graph(num_nodes, edges)
colored_nodes_large = color_graph(large_graph)

for node, color in sorted(colored_nodes_large.items()):
    print(f"Node {node} has color {color}")

print("Test with higher degree graph:")
num_nodes = 200
edges = [(i, (i + 1) % num_nodes) for i in range(num_nodes)] + [(i, (i + 2) % num_nodes) for i in range(num_nodes)]

larger_degree_graph = initialize_graph(num_nodes, edges)
colored_nodes_larger_degree = color_graph(larger_degree_graph)

for node, color in sorted(colored_nodes_larger_degree.items()):
    print(f"Node {node} has color {color}")