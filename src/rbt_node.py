class Node:
    def __init__(self, data, color=1): # Mặc định node mới là Đỏ
        self.data = data
        self.color = color 
        self.left = None
        self.right = None
        self.parent = None