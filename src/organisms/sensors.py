class Eyes:
    def __init__(self, size):
        self.size = size
        self.translation = {"danger" : 0, "empty" : 1, "food" : 2}


    def sight(self, config, world, x_pos, y_pos):
        view = []
        for row in range(-self.size, self.size + 1, 1):
            for tile in range(-self.size, self.size + 1, 1):
                if y_pos + row >= 0 and y_pos + row < config.column_length and x_pos + tile >= 0 and x_pos + tile < config.row_length:
                    view.append(self.translation[world[y_pos + row][x_pos + tile].content])
                else:
                    view.append(self.translation["danger"])
        return view