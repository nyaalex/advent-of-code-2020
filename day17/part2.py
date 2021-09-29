import gameOfLife


class GameHypercube(gameOfLife.GameHandler):
    def load_board(self, filename):

        board_file = open(filename)
        self.main_board = gameOfLife.CellSpace(4)
        cell_val = {
            '.': 0,
            '#': 1,
        }

        for x, line in enumerate(board_file):
            for y, cell in enumerate(line.strip()):
                self.main_board[x, y, 0, 0] = cell_val[cell]

        self.t = 0
        board_file.close()


if __name__ == '__main__':
    conway_hypercube = GameHypercube()
    conway_hypercube.load_board("input")

    for i in range(6):
        conway_hypercube.update()

    print(conway_hypercube.count_occupied())