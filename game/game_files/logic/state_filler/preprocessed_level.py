class preprocessed_level:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.t = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]
        self.options = {}
