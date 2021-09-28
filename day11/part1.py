class GameBoard:
    def __init__(self):
        self.arr = []
        self.max_x = 0
        self.max_y = 0
        self.t = 0

        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

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
        new_board = [[0] * self.max_y for _ in range(self.max_x)]
        changed = False

        for x in range(self.max_x):
            for y in range(self.max_y):
                current_cell = self.arr[x][y]

                result = self.rule(x, y)
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

    def rule(self, x, y):
        floor = '.'
        occupied = '#'
        empty = 'L'

        current_cell = self.arr[x][y]
        if current_cell == floor:
            return floor

        occupied_count = 0
        for dx, dy in self.directions:
            sub_x, sub_y = x + dx, y + dy
            if sub_y not in (-1, self.max_y) and \
                    sub_x not in (-1, self.max_x):

                if self.arr[sub_x][sub_y] == occupied:
                    occupied_count += 1

        if occupied_count >= 4:
            return empty
        elif current_cell == empty and occupied_count == 0:
            return occupied
        else:
            return current_cell


if __name__ == '__main__':
    board = GameBoard()
    board.load_board("input")

    flag = True
    while flag:
        flag = board.update()

    print(board.count_occupied())
