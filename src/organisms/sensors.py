class Eyes:
    def __init__(self, size):
        self.size = size
        self.translation = {"danger" : -1, "empty" : 0, "food" : 1}
        self.org_translation = {"danger" : -0.5, "empty" : 0.5, "food" : 0.5}

    # turns content of all tiles in a diamond shape into a list
    def sight(self, inputs, world, x_pos, y_pos):
        # adds relative position in world to inputs
        view = [x_pos / inputs["row_length"], y_pos / inputs["column_length"]]
        for row in range(-self.size, self.size + 1, 1):
            # when abs(row) is big, tile will be smaller
            # this creates a shape that is wide in the middle and small on the top and bottom 
            for tile in range(-self.size + abs(row), self.size + 1 - abs(row), 1):
                # converts content to numbers for network input
                if y_pos + row >= 0 and y_pos + row < inputs["column_length"] and x_pos + tile >= 0 and x_pos + tile < inputs["row_length"]:
                    if world[y_pos + row][x_pos + tile].has_organism:
                        # sees tiles with organisms different to those without
                        view.append(self.org_translation[world[y_pos + row][x_pos + tile].content])
                    else:
                        view.append(self.translation[world[y_pos + row][x_pos + tile].content])
                else:
                    # every tile outside of the world is seen as danger
                    view.append(self.translation["danger"])
        return view