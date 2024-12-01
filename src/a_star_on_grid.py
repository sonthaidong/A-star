import heapq
from node import Node


def a_star(start, end, grid):
    # Deltas for moving in the 4 directions (up, down, left, right)
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Hàm tính toán ước lượng chi phí heuristic (Sử dụng khoảng cách Manhattan)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Danh sách mở (Open list) và đóng (Closed list)
    open_list = []
    closed_list = set()

    # Khởi tạo node bắt đầu và node đích
    start_node = Node(start, 0, heuristic(start, end))
    end_node = Node(end)

    # Đẩy node bắt đầu vào danh sách mở
    heapq.heappush(open_list, start_node)

    while open_list:
        # Lấy node có f nhỏ nhất từ danh sách mở
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Nếu đã tới đích, dựng lại đường đi
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Trả lại đường đi từ start đến end (đảo ngược lại)

        # Duyệt qua các neighbors
        for delta in neighbors:
            neighbor_pos = (
                current_node.position[0] + delta[0],
                current_node.position[1] + delta[1],
            )

            # Kiểm tra nếu neighbor là hợp lệ (trong grid và chưa được thăm)
            if (
                0 <= neighbor_pos[0] < len(grid)
                and 0 <= neighbor_pos[1] < len(grid[0])
                and grid[neighbor_pos[0]][neighbor_pos[1]] == 0
                and neighbor_pos not in closed_list
            ):

                # Tính toán chi phí g và h cho neighbor
                g = current_node.g + 1  # Chi phí di chuyển là 1 cho mỗi bước
                h = heuristic(neighbor_pos, end_node.position)
                neighbor_node = Node(neighbor_pos, g, h, current_node)

                # Kiểm tra nếu neighbor đã có trong open list với f nhỏ hơn
                if all(
                    neighbor_node.f < node.f
                    for node in open_list
                    if node.position != neighbor_pos
                ):
                    heapq.heappush(open_list, neighbor_node)

    return None  # Không tìm thấy đường đi


# Ví dụ về lưới và cách gọi thuật toán A*
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # Điểm bắt đầu
end = (4, 4)  # Điểm đích

path = a_star(start, end, grid)
if path:
    print("Đường đi từ", start, "đến", end, "là:", path)
else:
    print("Không thể tìm thấy đường đi.")
