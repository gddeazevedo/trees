RED   = 0
BLACK = 1

class Node:
    def __init__(self, data: int, color: RED | BLACK=BLACK):
        self.color = color
        self.left = None
        self.right = None
        self.p = None
        self.data = data


class RedBlackTree:
    def __init__(self):
        pass
