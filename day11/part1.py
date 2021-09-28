class GameBoard:
    def __init__(self):
        self.arr = []
        self.max_x = 0
        self.max_y = 0
        self.t = 0

    def __repr__(self):
        return '\n'.join([''.join(i) for i in self.arr])

    def load_board(self, filename):
        board_file = open(filename)
        self.arr = []

        for line in board_file:
            line = line.strip()
            if line:
                self.arr.append(list(line))

        self.max_x = len(self.arr)
        self.max_y = len(self.arr[0])
        self.t = 0
        board_file.close()

    def update(self):
        new_board = [[0]*self.max_y for _ in range(self.max_x)]
        changed = False

        for x in range(self.max_x):
            for y in range(self.max_y):
                current_cell = self.arr[x][y]
                adj = []
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        sub_x = x + dx
                        sub_y = y + dy
                        if (sub_x, sub_y) != (x, y) and \
                                sub_y not in (-1, self.max_y) and \
                                sub_x not in (-1, self.max_x):

                            adj.append(self.arr[sub_x][sub_y])

                result = self.rule(current_cell, adj)
                changed = changed or result != current_cell
                new_board[x][y] = result

        self.arr = new_board
        self.t += 1
        # print("==========\nT=%s\n%s" % (self.t, self))
        return changed

    def count_occupied(self):
        count = 0
        for row in self.arr:
            count += row.count('#')
        return count

    @staticmethod
    def rule(current_cell, adjacent):
        floor = '.'
        occupied = '#'
        empty = 'L'
        if current_cell == floor:
            return floor
        elif adjacent.count(occupied) >= 4:
            return empty
        elif current_cell == empty and occupied not in adjacent:
            return occupied
        else:
            return current_cell


board = GameBoard()
board.load_board("input")

changed = True
while changed:
    changed = board.update()

print(board.count_occupied())
