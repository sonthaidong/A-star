class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position  # Vị trí của node (x, y)
        self.g = g  # Chi phí từ điểm bắt đầu đến node này
        self.h = h  # Ước lượng chi phí từ node đến đích
        self.f = g + h  # Tổng chi phí ước lượng
        self.parent = parent  # Cha của node này

    # magic method/dunder method để so sánh các node dựa trên giá trị f
    def __lt__(self, other):
        # So sánh các node dựa trên giá trị f để đảm bảo heapq có thể hoạt động (min heap)
        return self.f < other.f
