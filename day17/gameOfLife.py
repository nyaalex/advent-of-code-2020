class CellSpace:
    def __init__(self, dimensions):
        self.EMPTY = 0
        self.DIRECTIONS = list(self.__gen_directions(dimensions))
        i = self.DIRECTIONS.index((0,)*dimensions)
        self.DIRECTIONS.pop(i)

        self.DIMENSIONS = dimensions

        self.cells = dict()
        self.to_check = set()

    @staticmethod
    def __gen_directions(n):
        if n == 0:
            yield tuple()
        else:
            for i in CellSpace.__gen_directions(n - 1):
                yield (-1,) + i
                yield (0,) + i
                yield (1,) + i

    def __get(self, key):
        if key in self.cells:
            return self.cells[key]
        else:
            return self.EMPTY

    def __getitem__(self, key):
        current_cell = self.__get(key)
        adjacent = []
        for delta in self.DIRECTIONS:
            sub_key = tuple((a + b for a, b in zip(delta, key)))
            adjacent.append(self.__get(sub_key))
        return current_cell, tuple(adjacent)

    def __setitem__(self, key, value):
        self.cells[key] = value
        self.to_check.add(key)
        if value == 0:
            delete = True
            for delta in self.DIRECTIONS:
                sub_key = tuple((a + b for a, b in zip(delta, key)))
                delete = delete and self.__get(sub_key) == 0
            if delete:
                self.cells.pop(key)
                self.to_check.remove(key)
        else:
            for delta in self.DIRECTIONS:
                sub_key = tuple((a + b for a, b in zip(delta, key)))
                self.to_check.add(sub_key)

    def __repr__(self):
        if self.DIMENSIONS == 2:
            get_x = lambda x: x[0]
            get_y = lambda x: x[1]

            min_x, max_x = min(self.to_check, key=get_x)[0], max(self.to_check, key=get_x)[0]
            min_y, max_y = min(self.to_check, key=get_y)[1], max(self.to_check, key=get_y)[1]

            output = ""
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    output += f"{self[x,y][0]}"
                output += '\n'

            return output
        else:
            return self


class GameHandler:
    def __init__(self):
        self.t = 0
        self.main_board = CellSpace(2)

    def update(self):
        next_board = CellSpace(self.main_board.DIMENSIONS)

        for cell_pos in self.main_board.to_check:
            cell, adjacent = self.main_board[cell_pos]
            new_cell = self.rule(cell, adjacent)
            next_board[cell_pos] = new_cell

        self.main_board = next_board
        self.t += 1

    def count_occupied(self):
        return sum(self.main_board.cells.values())

    @staticmethod
    def rule(cell, adjacent):
        count = sum(adjacent)
        if count == 3:
            return 1
        elif cell == 1 and count == 2:
            return 1
        else:
            return 0


if __name__ == '__main__':
    gol_test = GameHandler()
    pattern_pi = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (2, 1),
        (2, 0),
    ]

    pattern_glider = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 1),
    ]

    for i in pattern_pi:
        gol_test.main_board[i] = 1

    print(gol_test.main_board)
    for i in range(6):
        gol_test.update()
        print(gol_test.main_board)

    gol_test.main_board = CellSpace(2)
    for i in pattern_glider:
        gol_test.main_board[i] = 1

    print(gol_test.main_board)
    for i in range(6):
        gol_test.update()
        print(gol_test.main_board)
