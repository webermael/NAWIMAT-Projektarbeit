class Eyes:
    def __init__(self, size):
        self.size = size
        self.translation = {"danger" : 0, "empty" : 0.4, "food" : 1}
        self.org_translation = {"danger" : 0, "empty" : 0.6, "food" : 0.8}

    def sight(self, inputs, world, x_pos, y_pos):
        view = [x_pos / inputs["row_length"], y_pos / inputs["column_length"]]
        for row in range(-self.size, self.size + 1, 1):
            for tile in range(-self.size + abs(row), self.size + 1 - abs(row), 1):
                if y_pos + row >= 0 and y_pos + row < inputs["column_length"] and x_pos + tile >= 0 and x_pos + tile < inputs["row_length"]:
                    if world[y_pos + row][x_pos + tile].has_organism:
                        view.append(self.org_translation[world[y_pos + row][x_pos + tile].content])
                    else:
                        view.append(self.translation[world[y_pos + row][x_pos + tile].content])
                else:
                    view.append(self.translation["danger"])
        return view