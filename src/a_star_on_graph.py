import heapq
import networkx as nx
import matplotlib.pyplot as plt
from node import Node


def draw_weighted_graph(graph, pos=None):
    # Tạo một đối tượng đồ thị trong NetworkX
    G = nx.Graph()

    # Thêm các đỉnh và cạnh vào đồ thị G
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Vẽ đồ thị với các vị trí đã cho (pos) hoặc tự động tính toán vị trí
    if pos is None:
        pos = nx.spring_layout(G)  # Chế độ sắp xếp tự động (spring layout)

    # Vẽ các đỉnh
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
    )

    # Vẽ các cạnh
    edges = G.edges()
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): f"{G[u][v]['weight']}" for u, v in edges}
    )

    # Hiển thị đồ thị
    plt.title("Visual Representation of Weighted Graph")
    plt.show()


def a_star(graph, start, end, heuristic):
    open_list = []
    closed_list = set()

    # Khởi tạo node bắt đầu và node đích
    start_node = Node(start, 0, heuristic[start])
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.name)

        # Nếu đến đích, tái tạo đường đi
        if current_node.name == end_node.name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Đảo ngược để lấy đường đi từ start đến end

        # Duyệt các neighbors của current_node
        for neighbor, weight in graph[current_node.name].items():
            if neighbor not in closed_list:
                g = current_node.g + weight  # Chi phí từ start đến neighbor
                h = heuristic[neighbor]  # Ước lượng chi phí từ neighbor đến end
                neighbor_node = Node(neighbor, g, h, current_node)

                # Thêm vào open_list nếu không có trong danh sách mở hoặc có f nhỏ hơn
                if not any(
                    neighbor_node.name == node.name and neighbor_node.f >= node.f
                    for node in open_list
                ):
                    heapq.heappush(open_list, neighbor_node)

    return None  # Nếu không có đường đi


# Đồ thị có trọng số
graph = {
    "A": {"B": 10, "C": 5},
    "B": {"A": 10, "C": 2, "E": 20},
    "C": {"A": 5, "B": 2, "D": 6, "G": 9},
    "D": {"C": 6, "E": 1, "H": 7},
    "E": {"B": 20, "C": 6, "D": 1, "F": 3, "G": 8},
    "F": {"E": 3, "G": 4, "J": 1},
    "G": {"C": 9, "E": 8, "F": 4, "H": 5, "I": 3},
    "H": {"D": 7, "G": 5, "I": 3, "L": 8},
    "I": {"C": 5, "G": 3, "H": 3, "M": 2},
    "J": {"F": 1, "K": 4},
    "K": {"J": 4, "L": 6},
    "L": {"H": 8, "K": 6, "M": 3},
    "M": {"I": 2, "L": 3, "N": 4},
    "N": {"M": 4, "O": 6},
    "O": {"N": 6, "P": 8},
    "P": {"O": 8},
}

# Hàm heuristic
heuristic = {
    "A": 15,
    "B": 12,
    "C": 9,
    "D": 6,
    "E": 13,
    "F": 10,
    "G": 8,
    "H": 4,
    "I": 5,
    "J": 14,
    "K": 7,
    "L": 3,
    "M": 2,
    "N": 1,
    "O": 0,
    "P": 0,
}

# Tìm đường đi từ A đến P
start = "A"
end = "P"
path = a_star(graph, start, end, heuristic)

if path:
    print(f"Đường đi từ {start} đến {end} là: {path}")
else:
    print("Không thể tìm thấy đường đi.")

draw_weighted_graph(graph)
